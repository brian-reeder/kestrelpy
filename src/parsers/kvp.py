""" Python toolkit for working with Key/Value pair strings. """
from .event_log_base import generate_base_document

def is_key_value_pair(event_log: str):
    """ Evaluates whether an event log is a Key/Value Pair. """
    if '|' not in event_log:
        return False
    if '=' not in event_log:
        return False

    return True

def parse(event_log: str) -> dict:
    """ Parse structured Key=Value pair events into documents. """
    document: dict = generate_base_document(event_log)
    document['__type__'] = 'KeyValuePair'
    for tok in [t.split('=') for t in event_log.split('|')]:
        document[tok[0]] = tok[1] if tok[1] is not None else ''

    return document
