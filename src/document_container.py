""" Document Container is a server object for holding event logs. """
from copy import deepcopy
from types import MappingProxyType

class DocumentContainer:
    """ A container object to securely hold event logs. """
    _event_id: int
    _events: list[MappingProxyType]

    def __init__(self):
        self._event_id = 0
        self._events = []

    def register_document(self, document: dict) -> None:
        """ Add a document to the DocumentContainer. """
        self._event_id = self._event_id + 1
        doc = deepcopy(document)
        doc['__event_id__'] = self._event_id
        self._events.append(doc)

    def get_events(self) -> list[MappingProxyType]:
        """ Return a deep copy of the events listing. """
        return deepcopy(self._events)
