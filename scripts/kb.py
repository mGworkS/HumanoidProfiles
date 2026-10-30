#!/usr/bin/env python3
"""Validate canonical records, build human views and export retrieval records."""
import argparse
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import yaml
from jsonschema import Draft202012Validator, FormatChecker
from screening import section as screening_section, live_claims
from presentation import rebase_markdown_links

ROOT = Path(__file__).resolve().parents[1]
DELIVERY = {
    'enthalten':'Im dokumentierten Lieferumfang enthalten',
    'konfigurationsabhaengig':'Werksfunktion der dokumentierten Konfiguration; Paket und Firmware prüfen',
    'zusatzpaket':'Zusatzpaket; Umfang und Preis separat',
    'projektintegration':'Projektintegration und Inbetriebnahme erforderlich',
    'eigene_entwicklung':'Eigene Anwendung, Policy oder Integration erforderlich',
    'demo':'Vorführung; Lieferumfang nicht bestätigt',
    'angekuendigt':'Angekündigt; noch keine bestätigte Lieferfunktion',
    'nicht_enthalten':'In dieser Edition nicht enthalten',
    'nicht_anwendbar':'Für diese Bauform oder Konfiguration nicht anwendbar',
    'unbekannt':'Lieferumfang und mögliche Zusatzkosten unbekannt',
}
CAPABILITY_KEYS = ['mobility.walking','mobility.running','mobility.jumping','mobility.dancing',
                   'mobility.steps_up','mobility.steps_down','mobility.uneven_ground','mobility.rubble',
                   'mobility.obstacles','mobility.self_recovery','manipulation.pick_place']
INTEGRATION_KEYS = ['navigation.scope','navigation.mapping','navigation.obstacle_avoidance',
                    'fleet.management','integration.erp','integration.wms','integration.wes',
                    'integration.mes','integration.api']
class StrictLoader(yaml.SafeLoader):
    pass

def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'Doppelter YAML Schlüssel: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)

def read_yaml(path):
    return yaml.load(path.read_text(encoding='utf-8'), Loader=StrictLoader)

def front(path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---\n'):
        raise ValueError(f'Front Matter fehlt: {path}')
    _, header, body = text.split('---\n', 2)
    return yaml.load(header, Loader=StrictLoader), body.strip()

def load(root=ROOT):
    sources = {p.stem: front(p)[0] for p in sorted((root/'quellen').glob('*.md'))}
    orgs = {p.parent.name: front(p)[0] for p in sorted((root/'hersteller').glob('*/profil.md'))}
    robots = {}
    for p in sorted((root/'roboter').glob('*/profil.md')):
        meta, body = front(p)
        robots[p.parent.name] = (meta, read_yaml(p.with_name('fakten.yaml')), body)
    return sources, orgs, robots, read_yaml(root/'schema/merkmale.yaml')['metrics'], read_yaml(root/'schema/taxonomie.yaml')['axes']

def validate(root=ROOT):
    sources, orgs, robots, metrics, axes = load(root)
    errors = []
    validators = {p.name.split('.')[0]: Draft202012Validator(json.loads(p.read_text()), format_checker=FormatChecker()) for p in (root/'schema').glob('*.schema.json')}
    classification_specs=read_yaml(root/'schema/einordnungen.yaml')['values']
    classification_codes=set(json.loads((root/'schema/roboter.schema.json').read_text())['properties']['classification']['properties']['value']['enum'])
    if set(classification_specs)!=classification_codes:errors.append('Einordnungen: Anzeigenamen und Schemacodes stimmen nicht überein')
    for code,spec in classification_specs.items():
        if not spec.get('label') or not spec.get('description'):errors.append(f'Einordnung {code}: Anzeigename oder Erklärung fehlt')
    def check(kind, value, label):
        for error in validators[kind].iter_errors(value):
            errors.append(f'{label}: {list(error.path)}: {error.message}')
    def refs(ids, label):
        for sid in ids:
            if sid not in sources: errors.append(f'{label}: unbekannte Quelle {sid}')
    for sid, src in sources.items():
        check('quelle', src, sid)
        if src['id'] != sid: errors.append(f'{sid}: ID und Dateiname stimmen nicht überein')
    for oid, org in orgs.items():
        check('hersteller', org, oid); refs(org['source_ids'], oid)
        if org['id'] != oid: errors.append(f'{oid}: ID und Ordner stimmen nicht überein')
    for key, spec in metrics.items():
        check('merkmal', spec, key)
    all_ids = list(sources) + list(orgs) + list(robots)
    if len(all_ids) != len(set(all_ids)): errors.append('IDs müssen über Entitätstypen eindeutig sein')
    for rid, (meta, data, body) in robots.items():
        check('roboter', meta, rid); check('fakten', data, rid)
        if meta['id'] != rid or data['robot_id'] != rid: errors.append(f'{rid}: ID und Ordner stimmen nicht überein')
        for oid in [meta['manufacturer_id']] + meta['developer_ids']:
            if oid not in orgs: errors.append(f'{rid}: unbekannte Organisation {oid}')
        refs(meta['classification']['source_ids'], rid)
        if meta.get('official_link'):
            refs([meta['official_link']['source_id']], rid)
            if not meta['official_link']['url'].startswith('https://'): errors.append(f'{rid}: offizieller Link muss HTTPS verwenden')
        screening = meta.get('screening')
        if screening:
            refs(screening['source_ids'], rid)
            if screening['section']=='aktuell' and (not screening['source_ids'] or not screening['checked_at'] or screening['basis']=='bestandsimport'):
                errors.append(f'{rid}: aktuelle Auswahl braucht datierten Beleg jenseits des Bestandsimports')

        for tag in meta['tags']:
            if tag['id'] not in axes.get(tag['axis'], {}): errors.append(f'{rid}: unbekannter Tag {tag}')
            refs(tag['source_ids'], rid)
        for relation in meta['relations']:
            if relation['target_id'] not in robots: errors.append(f'{rid}: unbekanntes Beziehungsziel')
            if relation['target_id'] == rid: errors.append(f'{rid}: Selbstbeziehung')
        claims = data['claims']; ids = [c['id'] for c in claims]
        if len(ids) != len(set(ids)): errors.append(f'{rid}: doppelte Aussage ID')
        for required in [k for k,s in metrics.items() if s['core']]:
            if not any(c['key'] == required for c in claims): errors.append(f'{rid}: Pflichtmerkmal fehlt: {required}')
        for c in claims:
            label=f'{rid}/{c["id"]}'
            refs([s['source_id'] for s in c['sources']], label)
            if c['key'] not in metrics:
                errors.append(f'{label}: Merkmal zuerst registrieren'); continue
            spec=metrics[c['key']]
            if c['unit'] != spec['unit']: errors.append(f'{label}: falsche Einheit')
            value=c['value']
            if value is not None:
                kind=spec['kind']
                if kind=='number' and (type(value) not in (int,float)): errors.append(f'{label}: Zahl erwartet')
                if kind=='text' and not isinstance(value,str): errors.append(f'{label}: Text erwartet')
                if kind=='boolean' and type(value) is not bool: errors.append(f'{label}: Boolean erwartet')
                if kind=='range' and (not isinstance(value,list) or len(value)!=2 or any(type(v) not in (int,float) for v in value) or value[0]>value[1]): errors.append(f'{label}: Ungültiger Wertebereich')
                if kind=='date' and not re.fullmatch(r'\d{4}(-\d{2}(-\d{2})?)?',str(value)): errors.append(f'{label}: Datum erwartet')
            if c['supersedes'] and c['supersedes'] not in ids: errors.append(f'{label}: ersetzte Aussage fehlt')
            if c['supersedes'] == c['id']: errors.append(f'{label}: Aussage ersetzt sich selbst')
            if c['status'] not in ['unbekannt','nicht_anwendbar','nicht_veroeffentlicht'] and c['evidence']=='keine': errors.append(f'{label}: Evidenzart fehlt')
            delivery=c['context'].get('bereitstellung')
            if delivery and delivery not in DELIVERY:errors.append(f'{label}: unbekannter Lieferumfang {delivery}')
            if delivery=='enthalten' and (c['status']!='belegt' or c['evidence'] in ['herstellerdemo','redaktionelle_einordnung','projektkatalog','keine']):
                errors.append(f'{label}: Lieferumfang braucht passenden Produkt oder Kundenbeleg; Demo genügt nicht')
        for section in ['offers','events','extensions','media']:
            values=data[section]
            if len({v['id'] for v in values}) != len(values): errors.append(f'{rid}: doppelte IDs in {section}')
        for offer in data['offers']:
            refs(offer['source_ids'],rid)
            if offer['provider_id'] not in orgs: errors.append(f'{rid}: Anbieter unbekannt')
            if offer['price'] is not None and offer['currency'] is None: errors.append(f'{rid}: Währung fehlt')
            if offer['status']=='bestaetigt' and (not offer['regions'] or not offer['audiences']): errors.append(f'{rid}: Angebotsumfang fehlt')
        for event in data['events']: refs(event['source_ids'],rid)
        for extension in data['extensions']:
            if not set(extension['claim_ids']).issubset(ids): errors.append(f'{rid}: Erweiterung verweist auf fehlende Aussage')
        for media in data['media']:
            refs([media['source_id']],rid)
            if media['local_path']:
                p=(root/'roboter'/rid/media['local_path']).resolve()
                if not p.is_relative_to((root/'roboter'/rid).resolve()) or not p.is_file(): errors.append(f'{rid}: ungültiger Medienpfad')
                elif not media['sha256'] or hashlib.sha256(p.read_bytes()).hexdigest()!=media['sha256']: errors.append(f'{rid}: Medienprüfsumme stimmt nicht')
    if errors: raise ValueError('\n'.join(errors))
    return len(robots)

def active_claims(data):
    return live_claims(data)

def ai_records(data):
    """Explicit AI relations; a simulated workflow is never implicit hardware support."""
    return [{'claim_id':c['id'],'key':c['key'],'system':c['context'].get('system',c['value']),
             'version':c['context'].get('version'),'role':c['context'].get('rolle'),
             'relationship':c['context'].get('bezug'),'status':c['status'],
             'context':c['context'],'source_ids':[s['source_id'] for s in c['sources']]}
            for c in active_claims(data) if c['key'] in ['software.ai_stack','software.compatible_models','software.related_research'] and c['value'] is not None]

def capability_records(data):
    return [{'claim_id':c['id'],'key':c['key'],'value':c['value'],'status':c['status'],
             'delivery':c['context'].get('bereitstellung','unbekannt'),'context':c['context'],
             'source_ids':[s['source_id'] for s in c['sources']]}
            for c in active_claims(data) if c['key'] in CAPABILITY_KEYS+INTEGRATION_KEYS]

def procurement_offers(data, as_of, region=None, audience=None, max_age=90):
    """No inference from classification, product pages or absence of data."""
    result=[]
    for o in data['offers']:
        age=(as_of-date.fromisoformat(o['checked_at'])).days
        if o['status']!='bestaetigt' or o['mode'] not in ['kauf','miete','leasing','raas'] or not 0<=age<=max_age: continue
        if region and region not in o['regions']: continue
        if audience and audience not in o['audiences']: continue
        result.append(o)
    return result

def esc(v): return str(v).replace('|','\\|').replace('\n',' ')
def display(c):
    if c['value'] is None: return {'unbekannt':'Unbekannt','nicht_anwendbar':'Nicht anwendbar','nicht_veroeffentlicht':'Nicht veröffentlicht'}.get(c['status'],c['status'])
    value=' bis '.join(map(str,c['value'])) if isinstance(c['value'],list) else str(c['value'])
    return value + (' '+c['unit'] if c['unit'] else '')
def write(root,path,text):
    p=root/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text.rstrip()+'\n',encoding='utf-8')

def editorial_sections(body):
    """Keep additional editorial sections instead of silently discarding them."""
    parts=re.split(r'^## (.+)\n',body,flags=re.MULTILINE)
    return {parts[i].strip():parts[i+1].strip() for i in range(1,len(parts),2)}

def media_label(item):
    return item['scope'] or item['id']

def media_links(items):
    return '<br>'.join(f'[{esc(media_label(m))}]({m["url"]})' for m in items) or 'Noch kein geprüfter Link erfasst'

def media_table(items, sources, prefix='../../'):
    text='| Typ | Original und Geltungsbereich | Version | Herkunft und Rechte |\n| --- | --- | --- | --- |\n'
    for m in items:
        source=sources[m['source_id']]
        text+=f'| {m["type"]} | [{esc(media_label(m))}]({m["url"]}) | {esc(m["version"] or "Nicht angegeben")} | [{esc(source["publisher"])}]({prefix}quellen/{m["source_id"]}.md). {esc(m["rights"])} |\n'
    return text

def render_claim(c,metrics,sources):
    text=f'### {c["id"].replace("_"," ")}\n\n**{metrics[c["key"]]["label"]}:** {display(c)}. Status: {c["status"]}. Evidenz: {c["evidence"]}.\n\n'
    if c['context']:text+='Bedingungen: '+esc('; '.join(f'{k}: {v}' for k,v in c['context'].items()))+'\n\n'
    for ref in c['sources']:
        src=sources[ref['source_id']]
        text+=f'* [{src["title"]}](../../quellen/{src["id"]}.md), Fundstelle: {ref["locator"]}. Zugang: {src["access_method"]}. Aussage geprüft: {c["checked_at"]}.\n'
    return text+'\n'

def capability_table(data, keys, metrics):
    claims=active_claims(data)
    text='| Funktion | Was ist belegt? | Direkt nutzbar oder Zusatzaufwand? | Bedingungen und Nachweis |\n| --- | --- | --- | --- |\n'
    for key in keys:
        spec=metrics[key]
        selected=[c for c in claims if c['key']==key]
        if not selected:
            text+=f'| {spec["label"]} | Nicht erfasst | Unbekannt | Kein bestätigter Eintrag |\n'
        for c in selected:
            delivery=DELIVERY[c['context'].get('bereitstellung','unbekannt')]
            detail='; '.join(v for k,v in c['context'].items() if k!='bereitstellung')
            ref=f'[{c["status"]} / {c["evidence"]}](#{c["id"].replace("_","-")})'
            text+=f'| {spec["label"]} | {esc(display(c))} | {delivery} | {esc(detail)} {ref} |\n'
    return text

def generate(root=ROOT):
    validate(root)
    sources, orgs, robots, metrics, axes=load(root)
    classification_specs=read_yaml(root/'schema/einordnungen.yaml')['values']
    generated='<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->\n\n'
    for rid,(meta,data,body) in robots.items():
        claims=active_claims(data)
        sections=editorial_sections(body)
        text=generated+f'# {meta["name"]}\n\n[Katalog](../../KATALOG.md) · [Herstellerübersicht](../../HERSTELLER.md) · [Einordnung und alle Tags](../../docs/einordnung_und_tags.md)\n\n'+sections.get('Einordnung','')+'\n\n'
        pictures=[m for m in data['media'] if m['type'] in ['foto','rendering']]
        videos=[m for m in data['media'] if m['type']=='video']
        documents=[m for m in data['media'] if m['type'] in ['datenblatt','handbuch','zeichnung']]
        if pictures:
            hero=pictures[0]
            text+=f'![{esc(hero["scope"])}]({hero["url"]})\n\n'
            text+=f'Bildquelle: [{sources[hero["source_id"]]["publisher"]}](../../quellen/{hero["source_id"]}.md). {hero["rights"]}\n\n'
        text+='## Steckbrief\n\n[Legende zu Merkmalen, Einheiten und Nachweisen](../../docs/legende.md)\n\n| Merkmal | Angabe | Nachweisstand |\n| --- | --- | --- |\n'
        text+=f'| Hersteller | [{esc(orgs[meta["manufacturer_id"]]["name"])}](../../hersteller/{meta["manufacturer_id"]}/README.md) | Organisationsprofil |\n'
        link=meta.get('official_link')
        if link:
            verification='geprüft' if link['verification']=='geprueft' else 'aus dem Bestand; noch nicht erneut geprüft'
            text+=f'| Offizielle Website | [{esc(link["url"])}]({link["url"]}) | {verification} |\n'
        else:
            candidates=meta['classification']['source_ids']
            text+='| Offizielle Website | Noch nicht bestätigt | '+', '.join(f'[Quellenhinweis]({sources[s]["url"]})' for s in candidates)+' |\n'
        text+='| Vorstellung und weitere Videos | '+media_links(videos)+' | Links auf Originale; Vorführung ist kein unabhängiger Test |\n'
        text+='| Datenblatt und Dokumentation | '+media_links(documents)+' | Versions und Konfigurationshinweise im Linktext beachten |\n'
        text+=f'| Bauform und Entität | {esc(meta["form"])}; {esc(meta["entity_type"])} | Geltungsbereich unten beachten |\n'
        classification=classification_specs[meta['classification']['value']]['label']
        text+=f'| Einordnung | [{esc(classification)}](../../docs/einordnung_und_tags.md#einordnung) | {esc(meta["classification"]["reason"])} |\n'
        text+=f'| Geltungsbereich | {esc(meta["scope"])} | Daten anderer Generationen werden nicht automatisch übertragen |\n'
        text+=f'| Prüfumfang | {esc(meta["maintenance"]["status"])} | {meta["maintenance"]["reviewed_at"] or "Noch nicht fachlich geprüft"} |\n'
        tag_bases={'herstellerziel':'Herstellerziel','dokumentierter_einsatz':'Dokumentierter Einsatz','dokumentierte_funktion':'Dokumentierte Funktion','redaktionelle_zuordnung':'Redaktionelle Zuordnung'}
        for axis,label,anchor in [('branche','Branchen','branchen'),('aufgabe','Aufgaben','aufgaben'),('umgebung','Umgebungen','umgebungen')]:
            tags=[t for t in meta['tags'] if t['axis']==axis]
            value='<br>'.join(f'[{esc(axes[axis][t["id"]]["label"])}](../../katalog/{axis}_{t["id"]}.md) ({tag_bases[t["basis"]]})' for t in tags) or 'Noch nicht zugeordnet'
            text+=f'| {label} | {value} | [Alle verfügbaren Tags](../../docs/einordnung_und_tags.md#{anchor}); keine Eignungsfreigabe |\n'
        text+='| Modellspezifische Besonderheiten | [Spezialinformationen zu diesem Typ](#modellspezifische-besonderheiten) | Freie Ergänzungen mit Belegbezug |\n'
        for key,spec in metrics.items():
            if not spec['overview']:continue
            selected=[c for c in claims if c['key']==key]
            if key in ['software.ai_stack','software.compatible_models']:
                known=[c for c in selected if c['value'] is not None]
                summary='<br>'.join(f'[{esc(c["value"])}](#{c["id"].replace("_","-")}) ({c["status"]})' for c in known) or ('Unbekannt' if selected else 'Nicht erfasst')
                text+=f'| {spec["label"]} | {summary} | [Rolle, Bezug und Bedingungen](#ki-modelle-und-software) |\n'
                continue
            for c in selected:
                conditions='; '.join(c['context'].values())
                val=display(c)+(f' ({conditions})' if conditions else '')
                anchor=c['id'].replace('_','-')
                text+=f'| {spec["label"]} | {esc(val)} | [{c["status"]} / {c["evidence"]}](#{anchor}) |\n'
        text+='\n'
        text+='## KI, Modelle und Software\n\n'
        ai=ai_records(data)
        if ai:
            text+='| System | Version | Rolle | Bezug und Grenzen | Nachweis |\n| --- | --- | --- | --- | --- |\n'
            for item in ai:
                text+=f'| {esc(item["system"])} | {esc(item["version"] or "Nicht benannt")} | {esc(item["role"] or "Noch nicht näher erfasst")} | {esc(item["relationship"] or "Bezug separat prüfen")}. {esc(item["context"].get("grenze",""))} | [{item["status"]}](#{item["claim_id"].replace("_","-")}) |\n'
        else:text+='Noch keine belegten modellspezifischen KI Systeme erfasst. Das bedeutet keine grundsätzliche Inkompatibilität.\n'
        text+='\nEingebaute Steuerung, Referenzintegration, Simulation und Forschungskooperation sind unterschiedliche Bezüge. Hardware und Softwareversion sowie Lizenz und Kundenrechte gemeinsam prüfen. Eine Plattform wie Isaac GR00T oder ein Rechner wie Jetson Thor belegen keine bestimmte vorinstallierte Modellversion.\n\n'
        text+='## Fähigkeiten und Lieferumfang\n\n'
        text+=capability_table(data,CAPABILITY_KEYS,metrics)
        text+='\n## Navigation, Flotte und Unternehmens IT\n\n'
        text+=capability_table(data,INTEGRATION_KEYS,metrics)
        text+='\nEine API oder ein SDK ist keine fertige ERP oder WMS Anbindung. Zusatzpakete, Cloud, Lizenzen, Kartenaufbau und Inbetriebnahme werden nur bei passendem Beleg als enthalten behandelt. Nicht erfasst und unbekannt bedeuten keine Verneinung.\n\n'
        text+='## Screening\n\n'
        screening=meta.get('screening',{})
        if screening:
            from views import ACCESS, SECTION_LABELS
            text+=f'**Ansicht:** {SECTION_LABELS[screening["section"]]}. **Zugang:** {ACCESS[screening["access"]]}.\n\n'
            text+=screening['reason']+'\n\n'
            text+='Einordnung geprüft: '+str(screening['checked_at'] or 'noch nicht')+'. Grundlage: '+screening['basis']+'. '+', '.join(f'[{s}](../../quellen/{s}.md)' for s in screening['source_ids'])+'\n\n'
        text+='\n## Beschaffung und Geschäftsmodell\n\n'
        if not data['offers']: text+='Kein konkretes aktuelles Angebot in diesem Bestand bestätigt. Das ist kein Nachweis der Nichtverfügbarkeit. Preis, Abo, RaaS und Integrationsleistungen bleiben offen.\n'
        for o in data['offers']:
            price=f'{o["price"]:g} {o["currency"]}' if o['price'] is not None else 'Nicht veröffentlicht oder nicht bestätigt'
            text+=f'| Angebot | Angabe |\n| --- | --- |\n| Modell und Umfang | {esc(o["configuration"])} |\n| Geschäftsmodell und Status | {o["mode"]}; {o["status"]} |\n| Preis | {price} |\n| Regionen und Zielgruppe | {esc(", ".join(o["regions"]))}; {esc(", ".join(o["audiences"]))} |\n| Abrechnung und Abo | {o["billing"]}; {o["subscription"]} |\n| Konditionen | {esc(o["term"] or "Nicht bestätigt")} |\n| Enthalten | {esc("; ".join(o["included"]) or "Nicht präzisiert")} |\n| Ausstieg | {esc(o["exit_conditions"] or "Nicht bestätigt")} |\n| Prüfung | {o["checked_at"]} |\n| Quellen | '+', '.join(f'[{sid}](../../quellen/{sid}.md)' for sid in o['source_ids'])+' |\n\n'
        for title,content in sections.items():
            if title not in ['Einordnung','Offene Entscheidungsfragen','Pflege','Modellspezifische Besonderheiten']:
                text+='\n## '+title+'\n\n'+content+'\n'
        questions=sections.get('Offene Entscheidungsfragen','Noch nicht erfasst.')
        text+='\n## Offene Entscheidungsfragen\n\n'+questions+'\n'
        text+='\n## Ereignisse und Termine\n\n'
        if not data['events']: text+='Keine zusätzlichen Ereignisse erfasst.\n'
        for e in data['events']:
            text+=f'* **{e["date"]}, {e["status"]}:** {e["description"]} '+', '.join(f'[{s}](../../quellen/{s}.md)' for s in e['source_ids'])+'\n'
        text+='\n## Modellspezifische Besonderheiten\n\n'
        special=sections.get('Modellspezifische Besonderheiten')
        if special:text+=special+'\n\n'
        if data['extensions']:
            for ex in data['extensions']:
                refs=', '.join(f'[{cid}](#{cid.replace("_","-")})' for cid in ex['claim_ids'])
                text+=f'**{ex["title"]}:** {ex["description"]}'+(f' Belege: {refs}.' if refs else '')+'\n\n'
        elif not special:text+='Noch keine zusätzlichen Spezialinformationen erfasst. Dieses Feld nimmt Besonderheiten auf, die sich durch die gemeinsamen Merkmale und Tags nicht ausreichend beschreiben lassen.\n'
        text+='\n## Medien und Dokumente\n\n[Alle Bilder und Videos](assets/README.md) · [Datenblätter und Dokumentation](dokumente/README.md). Externe Originale bleiben beim Anbieter.\n\n'
        if data['media']:text+=media_table(data['media'],sources)+'\n'
        text+='\n## Belege und Detailangaben\n\nDetails sind nach Fachgruppen aufklappbar. Unbekannte Angaben bedeuten keine Verneinung. Fehlende optionale Merkmale sind nicht erfasst.\n\n'
        known=[c for c in claims if c['value'] is not None or c['status']=='nicht_anwendbar']
        groups=list(dict.fromkeys(metrics[c['key']]['group'] for c in known))
        for group in groups:
            items=[c for c in known if metrics[c['key']]['group']==group]
            text+=f'<details>\n<summary>{group}: {len(items)} Angaben und Belege</summary>\n\n'
            text+=''.join(render_claim(c,metrics,sources) for c in items)+'\n</details>\n\n'
        unknown=[c for c in claims if c not in known]
        if unknown:
            text+=f'<details>\n<summary>Offene und nicht veröffentlichte Angaben ({len(unknown)})</summary>\n\n'
            text+=''.join(render_claim(c,metrics,sources) for c in unknown)+'\n</details>\n'
        write(root,f'roboter/{rid}/README.md',text)
        if data['media']:
            for sub,title,items in [('assets','Bilder und Videos',[m for m in data['media'] if m['type'] not in ['datenblatt','handbuch','zeichnung']]),('dokumente','Datenblätter und Dokumentation',documents)]:
                page=generated+f'# {meta["name"]}: {title}\n\n[Zurück zum Steckbrief](../README.md)\n\n'
                page+=media_table(items,sources,prefix='../../../') if items else 'Noch keine geprüften Verweise erfasst.\n'
                page+='\nVersion und Modellbezug stehen am jeweiligen Link. PDF, HTML Dokumentation und Formularzugänge sind ausdrücklich unterschieden. Externe Dateien sind kein mitindexierter Volltext.\n'
                write(root,f'roboter/{rid}/{sub}/README.md',page)
    for oid,org in orgs.items():
        body=front(root/f'hersteller/{oid}/profil.md')[1]
        text=generated+'[Herstellerübersicht](../../HERSTELLER.md) · [Katalog](../../KATALOG.md)\n\n'+body+'\n\n| Steckbrief | Angabe |\n| --- | --- |\n'
        website=f'[{org["website"]}]({org["website"]})' if org['website'] else 'Noch nicht bestätigt'
        text+=f'| Offizielle Website | {website} |\n| Organisationstyp | {org["organisationstyp"]} |\n| Profilstand | {org["reviewed_at"] or "Noch nicht geprüft"} |\n\n## Erfasstes Portfolio\n\n'
        for rid,(m,d,b) in robots.items():
            if oid in [m['manufacturer_id']]+m['developer_ids']: text+=f'* [{m["name"]}](../../roboter/{rid}/README.md)\n'
        text+='\n## Quellen\n\n'+''.join(f'* [{sources[s]["title"]}](../../quellen/{s}.md)\n' for s in org['source_ids'])
        write(root,f'hersteller/{oid}/README.md',text)
    text=generated+'# Hersteller und Entwicklungsorganisationen\n\n[Gesamter Roboterbestand](../katalog/README.md) · [Startseite](../README.md)\n\n'
    text+='Eine Organisation kann Hersteller, Entwickler oder Forschungspartner sein. Ungeprüfte Zuordnungen bleiben gekennzeichnet. Die Anzahl umfasst Modelle, Varianten und weitere erfasste Entitäten.\n\n'
    text+='| Organisation | Typ | Offizielle Website | Erfasste Profile | Profilstand |\n| --- | --- | --- | --- | --- |\n'
    for oid,org in sorted(orgs.items(),key=lambda item:item[1]['name'].casefold()):
        count=sum(oid in [m['manufacturer_id']]+m['developer_ids'] for m,d,b in robots.values())
        website=f'[{esc(org["website"])}]({org["website"]})' if org['website'] else 'Noch nicht bestätigt'
        text+=f'| [{esc(org["name"])}]({oid}/README.md) | {org["organisationstyp"]} | {website} | {count} | {org["reviewed_at"] or "Noch nicht geprüft"} |\n'
    write(root,'hersteller/README.md',text)
    write(root,'HERSTELLER.md',rebase_markdown_links(text,'hersteller'))
    from views import build_catalog
    build_catalog(root,sources,orgs,robots,metrics,axes,generated)

def export(root=ROOT, commit=None, as_of=None):
    validate(root)
    sources,orgs,robots,metrics,axes=load(root)
    if commit is None:
        try: commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True,stderr=subprocess.DEVNULL).strip()
        except subprocess.CalledProcessError: commit='uncommitted'
    as_of=as_of or date.today()
    policy=read_yaml(root/'schema/screening_policy.yaml')
    index=[];chunks=[]
    for rid,(m,d,body) in robots.items():
        meta={'robot_id':rid,'name':m['name'],'manufacturer_id':m['manufacturer_id'],'entity_type':m['entity_type'],'review_status':m['maintenance']['status'],'classification':m['classification']['value'],'form':m['form'],'tags':m['tags'],'scope':m['scope'],'commit':commit,'source_path':f'roboter/{rid}/fakten.yaml'}
        meta.update(screening_section=screening_section(m,d,as_of,policy),screening=m.get('screening'),official_link=m.get('official_link'))
        index.append({**meta,'claims':active_claims(d),'offers':d['offers'],'events':d['events'],'extensions':d['extensions'],'media':d['media'],'ai_systems':ai_records(d),'capabilities':capability_records(d)})
        for c in active_claims(d):
            text=f'{m["name"]}. Geltungsbereich: {m["scope"]} {metrics[c["key"]]["label"]}: {display(c)}. Status: {c["status"]}; Evidenz: {c["evidence"]}. Bedingungen: '+json.dumps(c['context'],ensure_ascii=False)
            chunks.append({**meta,'chunk_id':rid+':claim:'+c['id'],'kind':'claim','text':text,'claim':c,'source_ids':[s['source_id'] for s in c['sources']],'sources':[sources[s['source_id']] for s in c['sources']]})
        for kind,items in [('offer',d['offers']),('event',d['events'])]:
            for item in items: chunks.append({**meta,'chunk_id':rid+':'+kind+':'+item['id'],'kind':kind,'text':json.dumps(item,ensure_ascii=False),'record':item,'source_ids':item['source_ids'],'sources':[sources[s] for s in item['source_ids']]})
        for item in d['media']:
            sid=item['source_id']
            chunks.append({**meta,'chunk_id':rid+':media:'+item['id'],'kind':'media','text':json.dumps(item,ensure_ascii=False),'record':item,'source_ids':[sid],'sources':[sources[sid]],'notice':'Medienmetadaten und Originalverweis. Dateiinhalt nicht automatisch gelesen, transkribiert oder im Index enthalten.'})
        for item in d['extensions']:
            evidence_claims=[c for c in d['claims'] if c['id'] in item['claim_ids']]
            ids=sorted({ref['source_id'] for c in evidence_claims for ref in c['sources']})
            chunks.append({**meta,'chunk_id':rid+':extension:'+item['id'],'kind':'extension','text':item['title']+'. '+item['description'],'record':item,'source_ids':ids,'sources':[sources[sid] for sid in ids],'notice':'Individuelle Besonderheit; Nachweisstand aus den referenzierten Aussagen beachten.'})
        chunks.append({**meta,'chunk_id':rid+':editorial','kind':'editorial','source_path':f'roboter/{rid}/profil.md','text':body,'source_ids':m['classification']['source_ids'],'notice':'Redaktionelle Einordnung, Bestandsimport oder offene Fragen; keine aktuelle Verifikation ohne Aussagebeleg.','sources':[sources[s] for s in m['classification']['source_ids']]})
    write(root,'export/robots.json',json.dumps(index,ensure_ascii=False,indent=2))
    write(root,'export/chunks.jsonl','\n'.join(json.dumps(c,ensure_ascii=False) for c in chunks))
    manifest={'schema_version':'1.0','commit':commit,'chunk_ids':[c['chunk_id'] for c in chunks],'content_hashes':{c['chunk_id']:hashlib.sha256(json.dumps(c,sort_keys=True,ensure_ascii=False).encode()).hexdigest() for c in chunks}}
    write(root,'export/manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    return index,chunks

def check_links(root=ROOT):
    errors=[]
    for p in root.rglob('*.md'):
        if '.git' in p.parts: continue
        for link in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in link or link.startswith('#'): continue
            target=link.split('#',1)[0]
            if target and not (p.parent/target).exists(): errors.append(f'{p.relative_to(root)}: {link}')
    if errors: raise ValueError('Fehlende interne Links:\n'+'\n'.join(errors))

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command',choices=['validate','build','export','query'])
    parser.add_argument('--mode',choices=['procurement','reference','pipeline','screening'],default='reference')
    parser.add_argument('--region');parser.add_argument('--audience');parser.add_argument('--as-of',default=date.today().isoformat());parser.add_argument('--commit')
    args=parser.parse_args()
    try:
        if args.command=='validate': print(f'OK: {validate()} Roboter validiert')
        elif args.command=='build': generate();check_links();print('Ansichten erzeugt und interne Links geprüft')
        elif args.command=='export':
            index,chunks=export(commit=args.commit,as_of=date.fromisoformat(args.as_of));print(f'Export: {len(index)} Modelle, {len(chunks)} Abschnitte')
        else:
            validate();robots=load()[2];result=[]
            policy=read_yaml(ROOT/'schema/screening_policy.yaml')
            for rid,(m,d,b) in robots.items():
                offers=procurement_offers(d,date.fromisoformat(args.as_of),args.region,args.audience)
                sec=screening_section(m,d,date.fromisoformat(args.as_of),policy)
                if args.mode=='screening' and sec!='aktuell':continue
                if args.mode=='procurement' and not offers: continue
                if args.mode=='pipeline' and m['classification']['value']!='pipeline':continue
                result.append({'id':rid,'name':m['name'],'classification':m['classification']['value'],'eligible_offers':offers,'screening_section':sec,'access':m.get('screening',{}).get('access')})
            print(json.dumps({'mode':args.mode,'as_of':args.as_of,'region':args.region,'audience':args.audience,'results':result,'note':'Keine Treffer bedeuten keinen bestätigten passenden Datensatz, nicht weltweite Nichtverfügbarkeit.'},ensure_ascii=False,indent=2))
    except (ValueError,KeyError,yaml.YAMLError) as error:
        print(str(error),file=sys.stderr);sys.exit(1)
