# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:33:57 2019

@author: 17pd04
"""

import socket

date=''
beg_time=''
end_time=''
event=''
count=1

def new_event():
    date=client_socket.recv(1024).decode('ascii')
    beg_time=client_socket.recv(1024).decode('ascii')
    end_time=client_socket.recv(1024).decode('ascii')
    event=client_socket.recv(1024).decode('ascii')
    dataset.write(count,0,user)
    dataset.write(count,0,date)
    dataset.write(count,0,beg_time)
    dataset.write(count,0,end_time)
    dataset.write(count,0,event)
    count=count+1
    return;
        
def rem_event(date,beg_time):
    date=client_socket.recv(1024).decode('ascii')
    beg_time=client_socket.recv(1024).decode('ascii')
    return;
    
def upd_event(date,beg_time):
    date=client_socket.recv(1024).decode('ascii')
    beg_time=client_socket.recv(1024).decode('ascii')
    return;
    
def get_specific(date,beg_time):
    date=client_socket.recv(1024).decode('ascii')
    beg_time=client_socket.recv(1024).decode('ascii')
    return;
    
def get_range(date):
    date=client_socket.recv(1024).decode('ascii')
    return;

import xlsxwriter as xl

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 9995

server_socket.bind((host,port))
server_socket.listen(10)

dataset = xl.Workbook('data.xlsx')


while(1):
    client_socket,addr=server_socket.accept()
    
   
    user=client_socket.recv(1024).decode('ascii')
    choice=client_socket.recv(1024).decode('ascii')
    client_socket.send(choice.encode('ascii'))
    if(choice=='1'):
        new_event()
    elif(choice=='2'):
        rem_event(date,beg_time)
    elif(choice=='3'):
        upd_event(date,beg_time,end_time,event)
    elif(choice=='4'):
        get_specific(date,beg_time)
    elif(choice=='5'):
        get_range(date)
    
    client_socket.close()
    
    
    
