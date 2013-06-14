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

def process_data(data):
    mtype = mimetypes.guess_type(data) 
    print 'Server:',data
    
    
    databr = data.split("\n")
    print databr[0]
    datafile = databr[0].split()
    filetoRead = datafile[1]
    #print 'Mimetype:',mtype

while 1:
    client, address = s.accept()
    data = client.recv(size)
    print data
    databr = data.split("\n")
    print databr[0]
    datafile = databr[0].split()
    filetoRead = datafile[1]
    
   # process_data(data)    
    #print 'Server:',data
    #f = open (filetoRead ,'r')
    #R = f.read()
    #print R
    #client.send("POST /home/vineet/PYTHON/index.html  HTTP/1.1")
    for dirname, dirnames, filenames in os.walk('.'):
	for subdirname in dirnames:
	   client.send(os.path.join(dirname, subdirname))
	   client.send("\n")
	   
	for filename in filenames:
	   client.send(os.path.join(dirname, filename))
	   client.send("\n")
       #for name in filename:
      	#client.send(filename)
      	#client.send('\n')



    #client.send("<html>")
    #client.send(R)
    #client.send("</html>")
    client.close() 
