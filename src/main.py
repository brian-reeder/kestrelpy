""" brian-reeder/kestrelpy
A demo project for doing threat analysis on syslog events.
"""
import logging
import socketserver

from log_taxonomy import identify_logtype
from event_log_source import EventLogBase

LOG_FILE = 'kestrelpy_demo.log'
HOST, PORT = "0.0.0.0", 514

logging.basicConfig(
        level=logging.INFO,
        format='%(message)s',
        datefmt='',
        filename=f"logs/{LOG_FILE}",
        filemode='a'
    )

class SyslogUDPHandler(socketserver.BaseRequestHandler):
    """ UDP/514 - Syslog implementation """
    def handle(self):
        data = bytes.decode(self.request[0].strip())
        #socket = self.request[1]
        msg: str = str(data)
        print(f"{self.client_address[0]} : {msg}")

        event_type:type = identify_logtype(msg)
        parsed_log: EventLogBase = event_type(msg)
        print(parsed_log.get_fields())

        logging.info(msg)

if __name__ == "__main__":
    try:
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit): # pylint:disable=try-except-raise
        raise
    except KeyboardInterrupt:
        print("\nCtrl+C Pressed. Terminating.")
