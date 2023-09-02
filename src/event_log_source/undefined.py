""" Default event log type for unimplemented formats. """
from dataclasses import dataclass

from .event_log_base import EventLogBase

@dataclass
class UndefinedEvent(EventLogBase):
    """ Parset not implemented. """
    def __init__(self, event_log: str):
        super().__init__(event_log)
        self._fields['__type__'] = 'Undefined'
