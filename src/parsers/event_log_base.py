""" Base definition of an eventlog """
from datetime import datetime, timezone

def generate_base_document(event_log: str) -> dict:
    """ Creates a standard document base. """
    return {
        '__raw_event__': event_log,
        '__received_time__': str(datetime.now(timezone.utc)),
    }
