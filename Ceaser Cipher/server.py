# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket 
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
host = socket.gethostname()
port = 9995

server_socket.bind((host,port))
server_socket.listen(1)

client_socket,addr=server_socket.accept()

num = int(client_socket.recv(1024).decode("ascii"))
msg = client_socket.recv(1024).decode("ascii")
print("Recieved message : ",msg)
nmsg=""
for i in range(len(msg)):
    if(ord(msg[i])-num<97):
        temp=97-(ord(msg[i])-num)
        nmsg=nmsg+chr(123-temp)
    else:
        nmsg=nmsg+chr(ord(msg[i])-num)
client_socket.close()
print("Decoded message : ",nmsg)