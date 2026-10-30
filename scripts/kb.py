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

ROOT = Path(__file__).resolve().parents[1]
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

def generate(root=ROOT):
    validate(root)
    sources, orgs, robots, metrics, axes=load(root)
    generated='<!-- AUTOMATISCH ERZEUGT: python scripts/kb.py build. Nicht manuell bearbeiten. -->\n\n'
    for rid,(meta,data,body) in robots.items():
        claims=active_claims(data)
        text=generated+f'# {meta["name"]}\n\n'+body.split('## Einordnung\n\n',1)[-1].split('\n\n## Offene',1)[0]+'\n\n'
        text+=f'**Hersteller:** [{orgs[meta["manufacturer_id"]]["name"]}](../../hersteller/{meta["manufacturer_id"]}/README.md)  \n**Bauform:** {meta["form"]}  \n**Einordnung:** {meta["classification"]["value"]}  \n**Begründung:** {meta["classification"]["reason"]}  \n**Geltungsbereich:** {meta["scope"]}  \n**Prüfumfang:** {meta["maintenance"]["status"]}, {meta["maintenance"]["reviewed_at"] or 'noch nicht fachlich geprüft'}\n\n'
        text+='**Tags:** '+', '.join(axes[t['axis']][t['id']]['label']+' ('+t['basis']+')' for t in meta['tags'])+'\n\n'
        link=meta.get('official_link')
        if link:
            verification='geprüft' if link['verification']=='geprueft' else 'aus dem Bestand; noch nicht erneut geprüft'
            text+=f'**Offizielle Modellquelle:** [{link["url"]}]({link["url"]}) ({verification}).\n\n'
        else:
            candidates=meta['classification']['source_ids']
            text+='**Offizielle Modellquelle:** Noch nicht bestätigt. '+', '.join(f'[Bisheriger Quellenhinweis]({sources[s]["url"]})' for s in candidates)+'\n\n'
        text+='## Screening\n\n'
        screening=meta.get('screening',{})
        if screening:
            from views import ACCESS, SECTION_LABELS
            text+=f'**Ansicht:** {SECTION_LABELS[screening["section"]]}. **Zugang:** {ACCESS[screening["access"]]}.\n\n'
            text+=screening['reason']+'\n\n'
            text+='Einordnung geprüft: '+str(screening['checked_at'] or 'noch nicht')+'. Grundlage: '+screening['basis']+'. '+', '.join(f'[{s}](../../quellen/{s}.md)' for s in screening['source_ids'])+'\n\n'
        text+='## Steckbrief\n\n[Legende zu Merkmalen, Einheiten und Nachweisen](../../docs/legende.md)\n\n| Merkmal | Angabe | Nachweisstand |\n| --- | --- | --- |\n'

        for key,spec in metrics.items():
            if not spec['overview']: continue
            selected=[c for c in claims if c['key']==key]
            for c in selected:
                conditions='; '.join(c['context'].values())
                val=display(c)+(f' ({conditions})' if conditions else '')
                anchor=c['id'].replace('_','-')
                text+=f'| {spec["label"]} | {esc(val)} | [{c["status"]} / {c["evidence"]}](#{anchor}) |\n'
        text+='\n## Beschaffung und Geschäftsmodell\n\n'
        if not data['offers']: text+='Kein konkretes aktuelles Angebot in diesem Bestand bestätigt. Das ist kein Nachweis der Nichtverfügbarkeit. Preis, Abo, RaaS und Integrationsleistungen bleiben offen.\n'
        for o in data['offers']:
            text+=f'* **{o["mode"]}, {o["status"]}:** {o["configuration"]}. Regionen: {", ".join(o["regions"])}. Abrechnung: {o["billing"]}. Abo: {o["subscription"]}. Geprüft: {o["checked_at"]}. Quellen: '+', '.join(f'[{sid}](../../quellen/{sid}.md)' for sid in o['source_ids'])+'\n'
        questions=body.split('## Offene Entscheidungsfragen\n\n',1)[-1].split('\n## Pflege',1)[0]
        text+='\n## Offene Entscheidungsfragen\n\n'+questions+'\n'
        text+='\n## Ereignisse und Termine\n\n'
        if not data['events']: text+='Keine zusätzlichen Ereignisse erfasst.\n'
        for e in data['events']:
            text+=f'* **{e["date"]}, {e["status"]}:** {e["description"]} '+', '.join(f'[{s}](../../quellen/{s}.md)' for s in e['source_ids'])+'\n'
        text+='\n## Belege und Detailangaben\n\nUnbekannte Pflichtangaben werden gesammelt gezeigt. Andere fehlende Merkmale sind nicht erfasst und dürfen nicht als Nein interpretiert werden.\n\n'
        for c in claims:
            text+=f'### {c["id"].replace("_"," ")}\n\n**{metrics[c["key"]]["label"]}:** {display(c)}. Status: {c["status"]}. Evidenz: {c["evidence"]}.\n\n'
            if c['context']: text+='Bedingungen: '+esc('; '.join(f'{k}: {v}' for k,v in c['context'].items()))+'\n\n'
            for ref in c['sources']:
                src=sources[ref['source_id']]
                text+=f'* [{src["title"]}](../../quellen/{src["id"]}.md), Fundstelle: {ref["locator"]}. Zugang: {src["access_method"]}. Aussage geprüft: {c["checked_at"]}.\n'
        if data['extensions']:
            text+='\n## Individuelle Besonderheiten\n\n'
            for ex in data['extensions']: text+=f'**{ex["title"]}:** {ex["description"]} (Aussagen: {", ".join(ex["claim_ids"])}).\n\n'
        text+='\n## Medien und Dokumente\n\n[Medienablage](assets/README.md) · [Dokumentablage](dokumente/README.md). Originale werden nur mit dokumentierter Herkunft und Nutzungsrechten aufgenommen.\n'
        write(root,f'roboter/{rid}/README.md',text)
    for oid,org in orgs.items():
        body=front(root/f'hersteller/{oid}/profil.md')[1]
        text=generated+body+'\n\n## Erfasstes Portfolio\n\n'
        for rid,(m,d,b) in robots.items():
            if oid in [m['manufacturer_id']]+m['developer_ids']: text+=f'* [{m["name"]}](../../roboter/{rid}/README.md)\n'
        text+='\n## Quellen\n\n'+''.join(f'* [{sources[s]["title"]}](../../quellen/{s}.md)\n' for s in org['source_ids'])
        write(root,f'hersteller/{oid}/README.md',text)
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
        index.append({**meta,'claims':active_claims(d),'offers':d['offers'],'events':d['events']})
        for c in active_claims(d):
            text=f'{m["name"]}. Geltungsbereich: {m["scope"]} {metrics[c["key"]]["label"]}: {display(c)}. Status: {c["status"]}; Evidenz: {c["evidence"]}. Bedingungen: '+json.dumps(c['context'],ensure_ascii=False)
            chunks.append({**meta,'chunk_id':rid+':claim:'+c['id'],'kind':'claim','text':text,'claim':c,'source_ids':[s['source_id'] for s in c['sources']],'sources':[sources[s['source_id']] for s in c['sources']]})
        for kind,items in [('offer',d['offers']),('event',d['events'])]:
            for item in items: chunks.append({**meta,'chunk_id':rid+':'+kind+':'+item['id'],'kind':kind,'text':json.dumps(item,ensure_ascii=False),'record':item,'source_ids':item['source_ids'],'sources':[sources[s] for s in item['source_ids']]})
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
