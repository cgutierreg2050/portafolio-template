"""Cloud-shaped local data models. No SDKs, credentials or remote calls."""
import hashlib
import ipaddress
import re
from collections import Counter
from html import escape
from .common import timestamp, unique


def terraform_review(data):
    """Review a simplified plan-shaped fixture, not Terraform plan JSON compatibility."""
    findings = []
    for r in unique(data['resources']):
        if r['action'] not in {'create', 'update', 'delete', 'replace', 'no-op'}:
            raise ValueError('unknown resource action')
        if r['action'] in {'delete', 'replace'}:
            findings.append({'resource': r['id'], 'reason': 'destructive-change-needs-review'})
        if r.get('public_management'): findings.append({'resource': r['id'], 'reason': 'public-management-exposure'})
        missing = sorted({'owner', 'environment'} - set(r.get('tags', {})))
        if missing: findings.append({'resource': r['id'], 'reason': 'missing-tags', 'tags': missing})
    return {'changes': dict(Counter(r['action'] for r in data['resources'])), 'findings': findings,
            'review_passed': not findings, 'terraform_executed': False}


def graph_messages(data):
    """Build escaped HTML drafts and deterministic request keys; never sends mail."""
    size = data['batch_size']
    if not isinstance(size, int) or isinstance(size, bool) or not 1 <= size <= 20:
        raise ValueError('demo batch size must be between 1 and 20')
    unique(data['recipients'])
    drafts, invalid, seen = [], [], set()
    for r in data['recipients']:
        address = r['email'].strip().lower()
        if not re.fullmatch(r'[^\s@]+@[^\s@]+\.[^\s@]+', address):
            invalid.append(r['id']); continue
        if address in seen: continue
        seen.add(address)
        key = hashlib.sha256((data['campaign']+'|'+address).encode()).hexdigest()[:16]
        drafts.append({'id': key, 'to': address, 'subject': data['subject'],
                       'html': '<p>Hello '+escape(r['name'])+',</p><p>Synthetic portfolio message.</p>'})
    return {'batches': [drafts[i:i+size] for i in range(0, len(drafts), size)],
            'invalid_recipients': invalid, 'sent': 0,
            'idempotency_note': 'local tracking keys only; no Graph deduplication guarantee'}


def archive_candidates(data):
    """Candidate selection from explicit dates and holds; does not move documents."""
    cutoff, now = timestamp(data['cutoff']), timestamp(data['as_of'])
    if cutoff >= now: raise ValueError('cutoff must precede assessment date')
    candidates, exclusions = [], []
    for doc in unique(data['documents']):
        when = timestamp(doc['last_activity'])
        if when > now: reason = 'future-date-needs-review'
        elif doc['legal_hold']: reason = 'legal-hold'
        elif doc['retain_until'] and timestamp(doc['retain_until']) > now: reason = 'retention-active'
        elif when >= cutoff: reason = 'recent-activity'
        else: reason = None
        if reason: exclusions.append({'id': doc['id'], 'reason': reason})
        else: candidates.append({'id': doc['id'], 'bytes': doc['bytes']})
    return {'candidates': candidates, 'candidate_bytes': sum(d['bytes'] for d in candidates),
            'excluded': exclusions, 'files_moved': 0, 'savings_calculated': False}


def vpn_topology(data):
    """CIDR validation and declared route review; not connectivity verification."""
    local, cloud = ipaddress.ip_network(data['on_prem']), ipaddress.ip_network(data['azure'])
    if local.version != cloud.version: raise ValueError('address families must match')
    issues = []
    if local.overlaps(cloud): issues.append('address-space-overlap')
    vm = ipaddress.ip_address(data['vm_ip'])
    if vm not in cloud: issues.append('vm-outside-azure-network')
    routes = [ipaddress.ip_network(r) for r in data['routes_to_on_prem']]
    if not any(local.subnet_of(r) for r in routes if r.version == local.version):
        issues.append('on-prem-route-missing')
    if not data['dns_forwarding']: issues.append('dns-forwarding-not-declared')
    return {'issues': issues, 'topology_checks_pass': not issues, 'tunnel_tested': False}


def n8n_config(data):
    """Review a simplified deployment inventory; no Kubernetes objects are applied."""
    issues = []
    if data['replicas'] < 1: issues.append('no-replicas')
    if data['service_type'] != 'ClusterIP': issues.append('direct-service-exposure')
    if not data['persistent_storage']: issues.append('persistent-storage-missing')
    if not data['readiness_probe']: issues.append('readiness-probe-missing')
    if not data['cloudflare_access']: issues.append('access-policy-missing')
    if not data['tunnel']: issues.append('tunnel-missing')
    if not data['encryption_key_secret_ref']: issues.append('encryption-key-secret-reference-missing')
    return {'issues': issues, 'configuration_checks_pass': not issues,
            'deployment_performed': False, 'high_availability_validated': False}


def sharepoint_owners(data):
    """Propose additive ownership in a declared pilot; never remove the last owner."""
    active = set(data['active_users'])
    changes, deferred = [], []
    for site in unique(data['sites']):
        owners = sorted(set(site['owners']))
        if site['id'] not in data['pilot_sites']:
            deferred.append({'site': site['id'], 'reason': 'outside-pilot'}); continue
        target = site['proposed_owner']
        if target not in active:
            deferred.append({'site': site['id'], 'reason': 'target-not-active'}); continue
        if not site['backup_verified']:
            deferred.append({'site': site['id'], 'reason': 'backup-unverified'}); continue
        changes.append({'site': site['id'], 'before': owners, 'after': sorted(set(owners + [target])),
                        'action': 'no-change' if target in owners else 'add-owner-proposal'})
    return {'changes': changes, 'deferred': deferred, 'writes': 0}


def arc_inventory(data):
    """Reconcile fictional asset inventory with agent records by stable device ID."""
    agents = {row['id']: row for row in unique(data['agents'])}
    now = timestamp(data['as_of'])
    results = []
    for device in unique(data['inventory']):
        agent = agents.get(device['id'])
        if not agent: state = 'not-observed-in-arc'
        else:
            age = (now - timestamp(agent['last_seen'])).total_seconds()/3600
            state = 'clock-skew' if age < 0 else 'stale' if age > 24 else 'recently-observed'
        results.append({'id': device['id'], 'state': state})
    return {'devices': results, 'enrollment_performed': False}


def document_retrieval(data):
    """Small lexical baseline with ACL filtering and citations, not an LLM/RAG system."""
    terms = set(re.findall(r'\w+', data['query'].casefold()))
    matches = []
    for doc in unique(data['documents']):
        if data['principal'] not in doc['readers']: continue
        words = set(re.findall(r'\w+', doc['text'].casefold()))
        score = len(terms & words)
        if score:
            matches.append({'id': doc['id'], 'score': score, 'citation': doc['source'], 'text': doc['text']})
    matches.sort(key=lambda m: (-m['score'], m['id']))
    return {'matches': matches[:data['limit']], 'status': 'sources-found' if matches else 'no-evidence',
            'answer_generated': False, 'method': 'lexical-baseline'}
