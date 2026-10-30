"""Human screening tables; never mix archives and inaccessible research into selection."""
from collections import Counter
from datetime import date
from pathlib import Path
import yaml
from screening import section, live_claims

SECTION_LABELS={'aktuell':'Aktuelle Auswahl','historie':'Historie und frühere Generationen','forschung':'Forschungsplattformen ohne bestätigten externen Zugang','ungeklaert':'Noch zu prüfende Einträge'}
ACCESS={'bestellweg':'Kauf angeboten','vorbestellung':'Vorbestellung / Reservierung','anfrage':'Kaufanfrage','projektzugang':'Projektzugang','vorgestellt':'Vorgestellt / angekündigt','kein_bestaetigter_zugang':'Zugang nicht bestätigt','unbekannt':'Unbekannt'}
ENTITY={'modell':'Modell','variante':'Variante','familie':'Familie','entwicklungsprogramm':'Entwicklungsprogramm'}
def cell(value): return str(value).replace('|','\\|').replace('\n',' ')
def claim_cell(rid,data,keys):
    claims=live_claims(data)
    # Exact sourced numbers take precedence over secondary descriptive summaries.
    primary=[c for c in claims if c['key'] in keys and c['value'] is not None and c['evidence']!='projektkatalog']
    chosen=primary or [c for c in claims if c['key'] in keys and c['value'] is not None]
    if not chosen: return 'Nicht erfasst'
    if keys==['hardware.height','hardware.height_description']:
        descriptive=[c for c in chosen if c['key']=='hardware.height_description']
        chosen=descriptive or chosen
    out=[]
    for c in chosen:
        v=c['value']; v=' bis '.join(map(str,v)) if isinstance(v,list) else str(v)
        if c['unit']:v+=' '+c['unit']
        if c['key']=='hardware.payload_arm':v+=' je Arm'
        if c['key']=='hardware.payload_two_arms':v+=' beidhändig'
        if c['key']=='hardware.payload_walking':v+=' beim Gehen'
        if c['status']=='angekuendigt':v+=' (angekündigt)'
        if c['key']=='hardware.payload_arm' and c.get('context',{}).get('condition'):v+='; '+c['context']['condition']
        marker='K' if c['evidence']=='projektkatalog' else 'H' if c['evidence'].startswith('hersteller') else 'B'
        out.append(cell(v)+f' [{marker}](../roboter/{rid}/README.md#{c["id"].replace("_","-")})')
    return '<br>'.join(out)

def render_table(ids,robots,orgs,policy,as_of):
    text='| Roboter | Hersteller | Ursprungsland | Vorstellung | Verkaufsstart | Zugang / Stand | Höhe | Payload / Lastbezug |\n| --- | --- | --- | --- | --- | --- | --- | --- |\n'
    for rid in sorted(ids,key=lambda r:(orgs[robots[r][0]['manufacturer_id']]['name'].casefold(),robots[r][0]['name'].casefold())):
        m,d,b=robots[rid];sc=m.get('screening',{});marker='K' if sc.get('basis')=='projektkatalog' else 'B'
        access=ACCESS.get(sc.get('access'),'Unbekannt')
        sec=section(m,d,as_of,policy)
        if sec=='historie':access='Historisch; '+access
        elif sec=='forschung':access='Externer Zugang nicht bestätigt'
        elif sec=='ungeklaert':access='Aktualität / Zugang ungeklärt'
        name=cell(m['name'])+(' ('+ENTITY[m['entity_type']]+')' if m['entity_type'] not in ['modell','variante'] else '')
        access+=(' · '+sc['checked_at']) if sc.get('checked_at') else ''
        row=[f'[{name}](../roboter/{rid}/README.md)',f'[{cell(orgs[m["manufacturer_id"]]["name"])}](../hersteller/{m["manufacturer_id"]}/README.md)',claim_cell(rid,d,['identity.origin_country']),claim_cell(rid,d,['lifecycle.first_presented']),claim_cell(rid,d,['lifecycle.sales_start']),cell(access)+f' [{marker}](../roboter/{rid}/README.md#screening)',claim_cell(rid,d,['hardware.height','hardware.height_description']),claim_cell(rid,d,['hardware.payload_arm','hardware.payload_two_arms','hardware.payload_walking','hardware.payload_description'])]
        text+='| '+' | '.join(row)+' |\n'
    return text

def build_catalog(root,sources,orgs,robots,metrics,axes,generated,as_of=None):
    policy=yaml.safe_load((root/'schema/screening_policy.yaml').read_text())
    as_of=as_of or date.fromisoformat(policy['snapshot_date'])
    buckets={s:[rid for rid,(m,d,b) in robots.items() if section(m,d,as_of,policy)==s] for s in SECTION_LABELS}
    note='[Legende zu Merkmalen und Kürzeln](../docs/legende.md) · Stand: '+as_of.isoformat()+'. **K** = Projektkatalog, noch nicht erneut an jeder Herstellerquelle geprüft. **H** = Herstellerangabe. **B** = weiterer Beleg oder Einordnungsnachweis. Die Links führen zu Bedingungen und Quellen. Ursprungsland bezeichnet Entwicklung, nicht Fertigung. Eine Angebotsanfrage oder Vorstellung ist keine bestätigte Lieferfähigkeit.\n\n'
    specs={
        'aktuelle_auswahl':('Aktuelle Auswahl',buckets['aktuell'],'aktuell'),
        'gegenwaertig':('Aktuelle Auswahl',buckets['aktuell'],'aktuell'),
        'entwicklungspipeline':('Vorbestellungen und vorgestellte Entwicklungen',[r for r in buckets['aktuell'] if robots[r][0]['screening']['access'] in ['vorbestellung','vorgestellt']],'aktuell'),
        'historie':(SECTION_LABELS['historie'],buckets['historie'],'historie'),
        'forschungsplattformen':(SECTION_LABELS['forschung'],buckets['forschung'],'forschung'),
        'ungeprueft':(SECTION_LABELS['ungeklaert'],buckets['ungeklaert'],'ungeklaert')}
    for axis,tags in axes.items():
        for tid,tag in tags.items():
            members=[r for r,(m,d,b) in robots.items() if any(t['axis']==axis and t['id']==tid for t in m['tags'])]
            if axis=='branche' or members:specs[f'{axis}_{tid}']=(tag['label'],members,'category')
    def save(path,text):
        p=root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.rstrip()+'\n',encoding='utf-8')
    for key,(title,members,kind) in specs.items():
        text=generated+'# '+title+'\n\n'+note
        if key.startswith('umgebung_'):
            text+='Einsatzumgebung, keine Branche und kein Sicherheitsnachweis.\n\n'
            tid=key[len('umgebung_'):]
            if axes['umgebung'][tid].get('description'):text+=axes['umgebung'][tid]['description']+'\n\n'
        if kind=='category':
            current=[r for r in members if r in buckets['aktuell']]
            text+='## Aktuelle Auswahl\n\n'
            text+=render_table(current,robots,orgs,policy,as_of) if current else 'Derzeit kein ausreichend zugeordneter aktueller Kandidat im geprüften Screeningbestand. Das bedeutet keine weltweite Nichtverfügbarkeit.\n'
            # Separate actual tables, with the other groups collapsed to keep screening clear.
            for sec in ['forschung','ungeklaert','historie']:
                selected=[r for r in members if r in buckets[sec]]
                if selected:
                    text+=f'\n<details>\n<summary>{SECTION_LABELS[sec]} ({len(selected)})</summary>\n\n'+render_table(selected,robots,orgs,policy,as_of)+'\n</details>\n'
        else:
            text+=render_table(members,robots,orgs,policy,as_of) if members else 'Keine Einträge in dieser Ansicht.\n'
        if key=='entwicklungspipeline':
            text+='\n## Offene Termine\n\n'
            for rid in members:
                for event in robots[rid][1]['events']:
                    if event['status']=='angekuendigt':text+=f'* {robots[rid][0]["name"]}: {event["date"]}, {event["description"]}\n'
        text+='\n[Auswahlübersicht](aktuelle_auswahl.md) · [Gesamtbestand in getrennten Tabellen](gesamtbestand.md)\n'
        save(Path('katalog')/(key+'.md'),text)
    text=generated+'# Gesamter erfasster Bestand\n\n'+note+'Alle Profile bleiben erhalten. Für die Vorauswahl zuerst die [aktuelle Auswahl](aktuelle_auswahl.md) verwenden. Historie, Forschung und ungeklärte Einträge stehen in eigenen Tabellen.\n\n'
    for sec in ['aktuell','forschung','ungeklaert','historie']:
        text+='## '+SECTION_LABELS[sec]+f' ({len(buckets[sec])})\n\n'+render_table(buckets[sec],robots,orgs,policy,as_of)+'\n'
    save(Path('katalog/gesamtbestand.md'),text)
    valid=set(specs)|{'gesamtbestand'}
    for p in (root/'katalog').glob('*.md'):
        if p.stem not in valid and p.read_text().startswith('<!-- AUTOMATISCH'):p.unlink()
    counts=Counter(m['entity_type'] for m,d,b in robots.values())
    plural={'modell':'Modelle','variante':'Varianten','familie':'Familien','entwicklungsprogramm':'Entwicklungsprogramme'}
    text=generated+'# HumanoidProfiles\n\nWissensbasis zur Auswahl humanoider Roboter und zur branchenübergreifenden Recherche.\n\n'
    text+=f'**[Aktuelle Roboter vergleichen](katalog/aktuelle_auswahl.md): {len(buckets["aktuell"])} Einträge** mit Hersteller, Ursprungsland, Vorstellung, Verkaufsstart, Zugang, Höhe und Payload. Vorbestellungen und kommerziell vorgestellte Entwicklungen sind eingeschlossen und erkennbar. Die Auswahl wird durch dokumentierte Quellen und Aktualität begrenzt.\n\n'
    text+='**Wissensbestand:** '+str(len(robots))+' Profile ('+', '.join(str(n)+' '+plural[k] for k,n in sorted(counts.items()))+'). Unterschiedliche Varianten und Quellenstände beachten.\n\n'
    text+='**[Legende zu Spalten, Kürzeln und Nachweisen](docs/legende.md)**\n\n## Aktuelle Auswahl nach Branchen\n\nEin Roboter darf unter mehreren Branchen oder Aufgaben erscheinen. Alle Links zeigen auf dasselbe Profil. Die Zuordnung ist keine Eignungszusage. Kategorien bleiben auch ohne aktuellen Treffer sichtbar.\n\n'
    for tid,tag in axes['branche'].items():text+=f'* [{tag["label"]}](katalog/branche_{tid}.md)\n'
    text+='\n## Aufgaben\n\n'
    for key,(title,members,kind) in specs.items():
        if key.startswith('aufgabe_'):text+=f'* [{title}](katalog/{key}.md)\n'
    text+='\n## Einsatzumgebungen\n\n'
    for key,(title,members,kind) in specs.items():
        if key.startswith('umgebung_'):text+=f'* [{title}](katalog/{key}.md)\n'
    text+='\n## Weitere Ansichten\n\n* [Vorbestellungen und vorgestellte Entwicklungen](katalog/entwicklungspipeline.md)\n* [Forschungsplattformen ohne bestätigten externen Zugang](katalog/forschungsplattformen.md)\n* [Noch zu prüfende Einträge](katalog/ungeprueft.md)\n* [Historie und frühere Generationen](katalog/historie.md)\n* [Gesamtbestand in getrennten Tabellen](katalog/gesamtbestand.md)\n\n## Pflegen und erweitern\n\n* [Architektur](docs/architektur.md)\n* [Legende zu Merkmalen und Kürzeln](docs/legende.md)\n* [Screeningregeln](docs/screening.md)\n* [Datenregeln](docs/datenregeln.md)\n* [Pflegeprozess](docs/pflegeprozess.md)\n* [Steckbrief](docs/steckbrief.md)\n* [Vorlagen](vorlagen/README.md)\n* [Importnachweis](recherche/importe/README.md)\n* [Offene Recherchekandidaten](recherche/kandidaten/README.md)\n* [RAG und strukturierte Auswahl](docs/rag.md)\n* [Änderungen](CHANGELOG.md)\n\n## Lokal ausführen\n\n```sh\npython -m pip install -r requirements.txt\npython scripts/kb.py validate\npython scripts/kb.py build\npython -m unittest discover -s tests -v\npython scripts/kb.py export\npython scripts/kb.py query --mode screening\n```\n\nDie lesbaren Ansichten werden automatisch aus den Originaldaten erzeugt. Exportdateien werden nicht versioniert. Noch kein gehostetes RAG System und keine automatische Webrecherche eingerichtet.\n'
    save(Path('README.md'),text)
    return {s:len(ids) for s,ids in buckets.items()}
