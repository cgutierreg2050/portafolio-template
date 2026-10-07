"""Offline scheduling, health and recovery demonstrations."""
import heapq
import posixpath
from collections import Counter
from xml.etree import ElementTree
from .common import positive, timestamp, unique


def transcription(data):
    """First-fit batch scheduling under a declared GPU budget, no model execution."""
    capacity = positive(data['gpu_mb'], 'gpu_mb') * data['utilization_limit']
    if not 0 < data['utilization_limit'] <= 1: raise ValueError('invalid utilization limit')
    batches, rejected = [], []
    for job in unique(data['jobs']):
        memory = positive(job['estimated_mb'], 'estimated_mb')
        if memory > capacity:
            rejected.append(job['id']); continue
        batch = next((b for b in batches if b['estimated_mb'] + memory <= capacity), None)
        if batch is None:
            batch = {'jobs': [], 'estimated_mb': 0}; batches.append(batch)
        batch['jobs'].append(job['id']); batch['estimated_mb'] += memory
    return {'capacity_mb': capacity, 'batches': batches, 'rejected': rejected, 'audio_processed': 0}


def relocation(data):
    """Dependency-aware critical-path schedule without resource contention modeling."""
    tasks = {r['id']: r for r in unique(data['tasks'])}
    finished, active = {}, set()
    def visit(task_id):
        if task_id in finished: return finished[task_id]
        if task_id in active: raise ValueError('dependency cycle')
        if task_id not in tasks: raise ValueError('unknown dependency')
        task = tasks[task_id]; positive(task['days'], 'duration')
        active.add(task_id)
        start = max((visit(dep)['finish_day'] for dep in task['depends_on']), default=0)
        active.remove(task_id)
        finished[task_id] = {'start_day': start, 'finish_day': start + task['days']}
        return finished[task_id]
    for task_id in tasks: visit(task_id)
    duration = max((r['finish_day'] for r in finished.values()), default=0)
    return {'schedule': finished, 'critical_path_days': duration,
            'within_target': duration <= data['target_days'], 'resource_constraints_modeled': False}


def container_queue(data):
    """Simulated longest-job-first allocation, no containers or websites are started."""
    count = data['workers']
    if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= 100:
        raise ValueError('workers must be an integer from 1 to 100')
    workers = [(0, i) for i in range(count)]; heapq.heapify(workers)
    allocation = {str(i): [] for i in range(count)}
    jobs = unique(data['jobs'])
    for j in jobs: positive(j['cost'], 'job cost')
    for job in sorted(jobs, key=lambda j: (-j['cost'], j['id'])):
        load, worker = heapq.heappop(workers)
        allocation[str(worker)].append(job['id'])
        heapq.heappush(workers, (load + job['cost'], worker))
    return {'assignments': allocation, 'estimated_max_load': max(w[0] for w in workers),
            'containers_started': 0}


def ai_lab(data):
    """Arithmetic lower-bound memory estimate, explicitly excludes KV cache/activations."""
    bits = data['quantization_bits']
    if bits not in (4, 8, 16, 32): raise ValueError('unsupported precision')
    params = positive(data['parameters_billions'], 'parameters_billions')
    gpu = positive(data['gpu_gib'], 'gpu_gib')
    reserve = data['runtime_reserve_gib']
    if reserve < 0 or reserve >= gpu: raise ValueError('invalid runtime reserve')
    weights = params * 1e9 * bits / 8 / 1024**3
    return {'weights_gib': round(weights, 3), 'available_gib_after_reserve': gpu - reserve,
            'weights_fit': weights <= gpu - reserve, 'inference_validated': False,
            'excluded': ['kv-cache', 'activations', 'quantization-metadata', 'allocator-overhead']}


def glpi_inventory(data):
    """Separate schema loss, inventory mismatch and endpoint-protection evidence."""
    missing = sorted(set(data['schema_before']) - set(data['schema_after']))
    rows = []
    for endpoint in unique(data['endpoints']):
        actual = endpoint['onboarded'] and endpoint['service_running'] and endpoint['realtime']
        rows.append({'id': endpoint['id'], 'protection_evidence': bool(actual),
                     'inventory_mismatch': endpoint['inventory_protected'] != bool(actual),
                     'stale_signatures': endpoint['signature_age_hours'] > 48})
    return {'missing_tables': missing, 'schema_preserved': not missing,
            'endpoints': rows, 'database_modified': False}


def monitoring(data):
    """Combine capacity, availability and event severity into synthetic alerts."""
    alerts = []
    for host in unique(data['hosts']):
        issues = []
        if host['cpu_percent'] >= data['cpu_threshold']: issues.append('cpu')
        if host['disk_free_percent'] <= data['disk_free_threshold']: issues.append('disk')
        if not host['reachable']: issues.append('unreachable')
        if host['security_level'] >= data['security_threshold']: issues.append('security-event')
        if issues: alerts.append({'host': host['id'], 'issues': issues,
                                  'priority': 'critical' if 'unreachable' in issues else 'review'})
    return {'alerts': alerts, 'notifications_sent': 0}


def kvm_recovery(data):
    """Inspect supplied libvirt XML and inventory, without modifying disks or a VM."""
    if '<!DOCTYPE' in data['domain_xml'].upper() or '<!ENTITY' in data['domain_xml'].upper():
        raise ValueError('DTD/entity declarations are not accepted')
    domain = ElementTree.fromstring(data['domain_xml'])
    source = domain.find('./devices/disk/source')
    if source is None or 'file' not in source.attrib: raise ValueError('file disk source required')
    old = source.attrib['file']
    disks = data['available_disks']
    exact = old in disks
    candidates = [p for p in disks if posixpath.basename(p) == posixpath.basename(old)]
    proposal = old if exact else candidates[0] if len(candidates) == 1 else None
    next_step = 'inspect-console' if exact else 'backup-xml-before-path-review' if proposal else 'manual-disk-identification'
    return {'current_path': old, 'proposed_path': proposal, 'next_step': next_step,
            'bitlocker_limits_offline_inspection': data['bitlocker'],
            'ad_trust_resolved': False, 'vm_modified': False}


def weekly_report(data):
    """Deduplicate event identities and aggregate a half-open UTC reporting window."""
    start, end = timestamp(data['start']), timestamp(data['end'])
    if end <= start: raise ValueError('empty or reversed reporting window')
    identities, events, duplicates = {}, [], 0
    for event in data['events']:
        key = (event['agent'], event['id'])
        if key in identities:
            if identities[key] != event: raise ValueError('conflicting duplicate event')
            duplicates += 1; continue
        identities[key] = event
        if start <= timestamp(event['at']) < end: events.append(event)
    return {'start': start.isoformat(), 'end_exclusive': end.isoformat(),
            'event_count': len(events), 'duplicates': duplicates,
            'by_agent': dict(sorted(Counter(e['agent'] for e in events).items())),
            'high_or_critical': sum(e['level'] >= 12 for e in events), 'messages_sent': 0}
