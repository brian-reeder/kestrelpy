""" brian-reeder/kestrelpy
A demo project for doing threat analysis on syslog events.
"""
import logging
import socketserver

from document_container import DocumentContainer
from log_taxonomy import parse_log

LOG_FILE = 'kestrelpy_demo.log'
HOST, PORT = "0.0.0.0", 514

REPLAY_LOG = False
EVENTS = DocumentContainer()

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
        data: str = bytes.decode(self.request[0].strip())
        #socket = self.request[1]
        msg: str = str(data)
        print(f"{self.client_address[0]}: {msg}")
        doc = parse_log(msg)
        EVENTS.register_document(doc)
        logging.info(msg)

def load_from_log() -> None:
    """ Initialize the log server from a file. """
    with open(f"logs/{LOG_FILE}", 'r', encoding='utf-8') as log:
        for event in log:
            doc = parse_log(event)
            EVENTS.register_document(doc)

if __name__ == "__main__":
    if REPLAY_LOG:
        load_from_log()
    try:
        server = socketserver.UDPServer((HOST,PORT), SyslogUDPHandler)
        server.serve_forever(poll_interval=0.5)
    except (IOError, SystemExit): # pylint:disable=try-except-raise
        raise
    except KeyboardInterrupt:
        print("\nCtrl+C Pressed. Terminating.")
