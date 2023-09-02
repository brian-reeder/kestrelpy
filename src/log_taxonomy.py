""" Module for analyzing and processing event logs based on taxonomy. """
from types import ModuleType

import parsers

def identify_logtype(event_log:str) -> ModuleType:
    """ Analze the event log and return the appropriate parser module. """
    if parsers.is_key_value_pair(event_log):
        return parsers.kvp
    return parsers.undefined

def parse_log(event_log:str) -> dict:
    """ Process events logs and return parsed documents. """
    parser_type = identify_logtype(event_log)
    doc = parser_type.parse(event_log)
    return doc
