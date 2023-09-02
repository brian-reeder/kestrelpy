""" Base definition of an eventlog """
from copy import deepcopy
from datetime import datetime, timezone

class EventLogBase:
    """ Base event log class"""
    _fields: dict = {}
    def __init__(self, event_log: str):
        self._fields['__event__'] = event_log
        self._fields['__rcvd_time__'] = str(datetime.now(timezone.utc))

    def get_fields(self) -> dict:
        """ Return a dictionary of all fields. """
        return deepcopy(self._fields)

    def get(self, key: str) -> str:
        """ Return the value for the key if the key exists """
        return self._fields.get(key)
