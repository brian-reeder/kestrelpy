""" Default event log type for unimplemented formats. """
from .event_log_base import generate_base_document

def parse(event_log: str) -> dict:
    """ Parser not implemented. """
    document: dict = generate_base_document(event_log)
    document['__type__'] = 'Undefined'

    return document
