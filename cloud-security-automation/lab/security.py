"""Illustrative policy evaluation over JSON fixtures; never applies controls."""
import re
from .common import timestamp, unique


def dmarc(data):
    """Strict domain alignment only; accepts supplied auth results, does not verify DNS."""
    results = []
    for msg in unique(data['messages']):
        def aligned(a, b):
            return bool(a and b and a.casefold().rstrip('.') == b.casefold().rstrip('.'))
        spf = msg['spf'] == 'pass' and aligned(msg.get('mail_from'), msg.get('header_from'))
        dkim = any(sig['result'] == 'pass' and aligned(sig.get('domain'), msg.get('header_from'))
                   for sig in msg.get('dkim', []))
        ok = spf or dkim
        results.append({'id': msg['id'], 'spf_aligned': spf, 'dkim_aligned': dkim,
                        'strict_dmarc': 'pass' if ok else 'fail',
                        'review': 'forwarding-review' if msg.get('forwarded') and not ok else 'none',
                        'allowlist_change': False})
    return {'messages': results}


def app_control(data):
    """Toy hash/publisher rule matcher, not the Windows policy engine."""
    if data['mode'] not in {'audit', 'enforce'}:
        raise ValueError('mode must be audit or enforce')
    if any(rule.get('action') not in {'allow', 'deny'} for rule in data['rules']):
        raise ValueError('unknown rule action')
    def matches(rule, app):
        selectors = {k: rule[k] for k in ('sha256', 'publisher') if k in rule}
        return bool(selectors) and all(app.get(k) == v for k, v in selectors.items())
    decisions = []
    for app in unique(data['applications']):
        rules = [r for r in data['rules'] if matches(r, app)]
        denied = any(r['action'] == 'deny' for r in rules)
        allowed = any(r['action'] == 'allow' for r in rules)
        decision = 'deny' if denied or not allowed else 'allow'
        decisions.append({'id': app['id'], 'decision': decision, 'policy_mode': data['mode'],
                          'effective_action': 'log-only' if data['mode'] == 'audit' else decision})
    return {'decisions': decisions, 'deployment_performed': False}


def purview(data):
    """Classify synthetic record markers and propose restrictions; no real DLP scanning."""
    results = []
    for doc in unique(data['documents']):
        restricted = bool(re.search(r'\bDEMO-RECORD-\d{4}\b', doc['text']))
        protected = restricted or doc.get('label') == 'Confidential'
        results.append({'id': doc['id'], 'label': 'Confidential' if protected else 'General',
                        'external_share': 'block-proposal' if protected and doc['external'] else 'no-change',
                        'retention': 'preserve-legal-hold' if doc.get('legal_hold') else 'review-policy',
                        'content_returned': False})
    return {'documents': results, 'policy_applied': False}


def hardening(data):
    """Read-only triage: flag unknown privileged identities, MFA gaps and forwards."""
    findings = []
    for user in unique(data['users']):
        if user['privileged'] and not user['approved']:
            findings.append({'entity': user['id'], 'finding': 'unapproved-privileged-identity', 'priority': 'high'})
        if user['privileged'] and not user['mfa']:
            findings.append({'entity': user['id'], 'finding': 'privileged-mfa-gap', 'priority': 'high'})
    for rule in unique(data['forwarding_rules']):
        if rule['external'] and not rule['approved']:
            findings.append({'entity': rule['id'], 'finding': 'unapproved-external-forward', 'priority': 'high'})
    return {'findings': findings, 'automatic_deletion': False, 'sessions_revoked': False}


def pgp_context(data):
    """Recipient-key metadata check only; does not parse or decrypt OpenPGP packets."""
    now = timestamp(data['as_of'])
    matches = [key for key in unique(data['keys']) if key['id'] == data['recipient_subkey']]
    reasons = []
    key = matches[0] if matches else None
    if key is None:
        reasons.append('recipient-subkey-unavailable')
    else:
        if key.get('context') != data['execution_context']: reasons.append('execution-context-mismatch')
        if key.get('revoked'): reasons.append('key-revoked')
        if timestamp(key['expires']) <= now: reasons.append('key-expired')
        if 'encrypt' not in key['capabilities']: reasons.append('not-an-encryption-subkey')
        if not key.get('private_material_available'): reasons.append('private-key-unavailable-in-context')
    return {'metadata_ready': not reasons, 'reasons': reasons, 'decryption_performed': False,
            'transfer_performed': False}


def patch_pilot(data):
    """Model correlation and evidence-gated closure, never submit a patch job."""
    devices = {d['id']: d for d in unique(data['devices'])}
    seen = {}
    results = []
    for finding in data['findings']:
        key = (finding['device'], finding['cve'])
        if key in seen:
            if seen[key] != finding:
                raise ValueError('conflicting duplicate finding; review evidence')
            continue
        seen[key] = finding
        dev = devices.get(finding['device'])
        kb = data['cve_to_kb'].get(finding['cve'])
        if not dev or not dev.get('in_pilot'):
            status = 'out-of-scope'
        elif not kb:
            status = 'manual-mapping-required'
        elif kb in dev['installed_kbs'] and finding.get('post_scan_clear') is True:
            status = 'verified-closed'
        elif not dev['online']:
            status = 'defer-offline'
        elif dev['reboot_pending']:
            status = 'defer-pending-reboot'
        elif kb in dev['installed_kbs']:
            status = 'await-post-validation'
        else:
            status = 'candidate-for-reviewed-job'
        results.append({'device': finding['device'], 'cve': finding['cve'], 'kb': kb, 'status': status})
    return {'findings': results, 'jobs_submitted': 0}


def iis_exposure(data):
    """Assess provided configuration facts; performs no network or TLS probes."""
    now = timestamp(data['as_of'])
    checks = []
    for portal in unique(data['portals']):
        reasons = []
        if not portal['tls_to_origin']: reasons.append('origin-tls-missing')
        if not portal['waf']: reasons.append('waf-missing')
        if not portal['access_policy']: reasons.append('access-policy-missing')
        if portal['origin_public']: reasons.append('origin-bypass-exposure')
        if timestamp(portal['certificate_expires']) <= now: reasons.append('certificate-expired')
        checks.append({'id': portal['id'], 'review': reasons, 'fixture_checks_pass': not reasons})
    return {'portals': checks}


def ad_readiness(data):
    """Assess a supplied AD inventory; does not prove a production migration is safe."""
    controllers = {row['id']: row for row in unique(data['controllers'])}
    issues = []
    for dc in controllers.values():
        if not dc['replication_ok']: issues.append(f"{dc['id']}:replication")
        if not dc['dns_ok']: issues.append(f"{dc['id']}:dns")
        if not dc['time_sync_ok']: issues.append(f"{dc['id']}:time-sync")
    required = {'schema', 'naming', 'rid', 'pdc', 'infrastructure'}
    if set(data['fsmo']) != required: issues.append('incomplete-fsmo-inventory')
    for role, owner in data['fsmo'].items():
        if owner not in controllers: issues.append(f'{role}:unknown-owner')
    if not data['backup_restore_tested']: issues.append('restore-test-missing')
    if len(controllers) < 2: issues.append('single-domain-controller')
    return {'issues': issues, 'prechecks_clear': not issues, 'migration_state': 'planning',
            'roles_transferred': False}


def key_vault_plan(data):
    """Names-only plan. Real credential fields are refused, not redacted."""
    names, result = set(), []
    for entry in unique(data['entries']):
        if set(entry) - {'id', 'title'}:
            raise ValueError('only id and title metadata are accepted; do not supply secrets')
        name = re.sub('[^a-z0-9-]+', '-', entry['title'].lower()).strip('-')
        if not name or len(name) > 127: raise ValueError('invalid normalized name')
        if name in names: raise ValueError('normalized name collision')
        names.add(name)
        result.append({'source_id': entry['id'], 'proposed_name': name})
    return {'plan': result, 'secret_values_read': 0, 'azure_writes': 0}
