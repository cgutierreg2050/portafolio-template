"""Small validation helpers shared by the synthetic demonstrations."""
from datetime import datetime, timezone


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None:
        raise ValueError('timestamps must include a timezone')
    return parsed.astimezone(timezone.utc)


def unique(rows, key='id'):
    ids = [row[key] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError(f'duplicate {key}')
    return rows


def positive(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f'{name} must be positive')
    return value


def synthetic(data):
    if not isinstance(data, dict) or data.get('synthetic') is not True:
        raise ValueError('input must explicitly declare synthetic: true')
    return data
