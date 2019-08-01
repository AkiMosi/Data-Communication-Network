# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:27:46 2019

@author: akile
"""

import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=9995

server_socket.bind((host,port))
server_socket.listen(1)

client_socket,addr=server_socket.accept()

r=int(client_socket.recv(1024).decode('ascii'))
msg=client_socket.recv(1024).decode('ascii')

codelen=len(msg)
code=list(msg)
parcheck=[]

for i in range(r):
    parbit=0
    for j in range((2**i)-1,codelen,2**(i+1)):
        for k in range(2**i):
            if(j+k>codelen-1):
                break
            if(code[j+k]=='*'):
                continue
            elif(code[j+k]=='1'):
                parbit+=1
            else:
                continue
    parcheck.append(str(parbit.__and__(1)))

parcheck=parcheck[::-1]
pos=int(("".join(parcheck)),2)

if(pos==0):
    print('There is no error in the transmission')
else:
    print('There is an error in the position ',pos)

client_socket.close()