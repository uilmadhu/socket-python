#SERVERRRRRRRRRRRR

import socket

s=socket.socket()
port=12345 # PORT ADDRESS
s.bind(('192.168.2.102',port)) # IP ADDRESS OF SERVER
s.listen(5)
while True:
 c,addr=s.accept()
 print 'Got connection from',addr
 c.send('THANK YOU')
 print c.recv(1024)
