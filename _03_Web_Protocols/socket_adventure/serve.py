"""
serve.py
Instantiates a socket-adventure 'Server' and serves it on a specified port.
you should not need to make any changes in this file.
"""

import sys

from server import Server

try:
    port = int(sys.argv[1])
except IndexError:
    print("Please include a port number, e.g: python server.py 50000 ")

server = Server(port)
server.serve()
