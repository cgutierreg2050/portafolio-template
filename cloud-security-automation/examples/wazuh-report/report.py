"""Local portfolio demo using synthetic Wazuh-like data. No API calls."""
import argparse, csv, html, json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

def timestamp(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('Timestamp must include a timezone')
    return parsed.astimezone(timezone.utc)

def summarize(events, start=None, end=None):
    counts, seen = Counter(), set()
    for event in events:
        key = str(event['id'])
        occurred = timestamp(event['timestamp'])
        if start and occurred < start: continue
        if end and occurred >= end: continue
        if key in seen: continue
        level = event['rule']['level']
        if isinstance(level, bool) or not isinstance(level, int) or not 0 <= level <= 15:
            raise ValueError('Rule level must be an integer from 0 to 15')
        agent = str(event['agent']['name'])
        seen.add(key)
        severity = 'critical' if level >= 12 else 'high' if level >= 8 else 'other'
        counts[(agent, severity)] += 1
    return [{'agent': a, 'severity': s, 'events': n} for (a,s),n in sorted(counts.items())]

def csv_safe(value):
    text = str(value)
    return "'" + text if text.lstrip().startswith(('=', '+', '-', '@')) else text

def write_report(rows, out):
    out.mkdir(parents=True,exist_ok=True)
    with (out/'summary.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=['agent','severity','events'])
        writer.writeheader()
        writer.writerows({k:csv_safe(v) for k,v in row.items()} for row in rows)
    body=''.join('<tr>'+''.join('<td>'+html.escape(str(v))+'</td>' for v in r.values())+'</tr>' for r in rows)
    (out/'summary.html').write_text('<!doctype html><meta charset="utf-8"><title>Synthetic security report</title><h1>Synthetic security report</h1><p>Portfolio demonstration data.</p><table><tr><th>Agent</th><th>Severity</th><th>Events</th></tr>'+body+'</table>',encoding='utf-8')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True); p.add_argument('--out',type=Path,required=True)
    p.add_argument('--start',type=timestamp); p.add_argument('--end',type=timestamp)
    a=p.parse_args()
    if a.start and a.end and a.start >= a.end: p.error('--start must precede --end')
    rows=summarize(json.loads(a.input.read_text()),a.start,a.end)
    write_report(rows,a.out)
    print(json.dumps({'status':'ok','groups':len(rows),'unique_events':sum(r['events'] for r in rows)}))
if __name__=='__main__': main()
