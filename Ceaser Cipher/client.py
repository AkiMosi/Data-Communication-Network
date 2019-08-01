# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:28:38 2019

@author: 17pd04
"""
import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port=9995

client_socket.connect((host,port))
num=int(input("Enter the cipher number : "))
msg=input("Enter the message : ")
nmsg=""
for i in range(len(msg)):
    if(ord(msg[i])+num>122):
        temp=(ord(msg[i])+num)-122
        nmsg=nmsg+chr(96+temp)
    else:
        nmsg=nmsg+chr(ord(msg[i])+num)
print("Encoded Message : ",nmsg)
client_socket.send(str(num).encode("ascii"))
client_socket.send(nmsg.encode("ascii"))
client_socket.close()


