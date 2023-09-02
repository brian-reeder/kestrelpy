import event_log_source as logs

def identify_logtype(event_log:str) -> logs.EventLogBase:
    if logs.is_key_value_pair(event_log):
        return logs.KeyValuePair
    return logs.UndefinedEvent