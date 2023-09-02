""" Python toolkit for working with Key/Value pair strings. """
from dataclasses import dataclass

from .event_log_base import EventLogBase

def is_key_value_pair(event_log: str):
    """ Evaluates whether an event log is a Key/Value Pair. """
    if '|' not in event_log:
        return False
    if '=' not in event_log:
        return False

    return True

@dataclass
class KeyValuePair(EventLogBase):
    """ Parse event logs in format for Key/Value Pairs. """
    fields: dict = {}
    def __init__(self, event_log: str):
        super().__init__(event_log)
        self._fields['__type__'] = 'KeyValuePair'
        log_toks = event_log.split('|')
        for tok in [t.split('=') for t in log_toks]:
            self.fields[tok[0]] = tok[1] if tok[1] is not None else ''
