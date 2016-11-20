#CLIENTTTTTTTTTTTTTTT
import socket
import time

s=socket.socket()
port=12345
s.connect(('192.168.2.102',port)) # IP ADDRESS OF SERVER

s.send('HIIII')
print s.recv(1024)
s.close()
