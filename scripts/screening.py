"""Explicit screening rules shared by human views and machine exports."""
from datetime import date

def live_claims(data):
    replaced = {c['supersedes'] for c in data['claims'] if c['supersedes']}
    return [c for c in data['claims'] if c['id'] not in replaced and c['valid_until'] is None]

def section(meta, data, as_of, policy):
    record = meta.get('screening', {})
    if meta['classification']['value'].startswith('historisch') or meta['classification']['value']=='fruehere_generation' or record.get('section')=='historie':
        return 'historie'
    if record.get('section')=='forschung':
        return 'forschung'
    if record.get('section')!='aktuell' or record.get('basis')=='bestandsimport':
        return 'ungeklaert'
    if meta['entity_type'] not in policy['allowed_entities'] or record.get('access') not in policy['allowed_access']:
        return 'ungeklaert'
    if not record.get('source_ids') or not record.get('checked_at'):
        return 'ungeklaert'
    age = (as_of-date.fromisoformat(record['checked_at'])).days
    if not 0 <= age <= policy['max_evidence_age_days']:
        return 'ungeklaert'
    # Explicit evidence of closure or ended support overrides a stale manual inclusion.
    stopped = {'eingestellt','beendet','ausgemustert'}
    for c in live_claims(data):
        if c['key'] in ['lifecycle.production','lifecycle.development'] and c['status']=='belegt' and c['value'] in stopped:
            return 'historie'
    return 'aktuell'
