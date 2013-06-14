 #!/usr/bin/env python

"""
A simple echo server
"""

import socket
import os
import mimetypes
import string

host = 'localhost' 
port = 30000
backlog = 5
size = 10240
teststr="\n"
filetoRead = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)


while 1:
    client, address = s.accept()
    data = client.recv(size)
    print data
    client.send(data) 
    client.close() 
