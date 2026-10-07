#!/usr/bin/env python3
"""Run a portfolio simulation. Stdlib only; no network, subprocess or credential use."""
import argparse
import json
from pathlib import Path
from lab.common import synthetic
from lab.registry import HANDLERS

ROOT = Path(__file__).resolve().parent


def run(project, source=None):
    if project not in HANDLERS:
        raise ValueError('unknown project')
    src = Path(source) if source else ROOT / 'projects' / project / 'input.json'
    data = synthetic(json.loads(src.read_text(encoding='utf-8')))
    return {'project': project, 'synthetic': True, 'mode': 'offline-demonstration',
            'production_validation': False, 'result': HANDLERS[project](data)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', choices=sorted(HANDLERS))
    parser.add_argument('--input', type=Path, help='Explicitly synthetic JSON fixture')
    parser.add_argument('--output', type=Path, help='Optional local result path')
    args = parser.parse_args()
    try:
        result = run(args.project, args.input)
        text = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding='utf-8')
        else:
            print(text, end='')
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(2, f'Input error: {error}\n')


if __name__ == '__main__':
    main()
