# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:34:01 2019

@author: 17pd04
"""

import socket

date=''
beg_time=''
end_time=''
user=''
event=''
choice=''

def new_event():
    date=input("Enter the date : ")
    beg_time=input("Enter the Beginning Time : ")
    end_time=input("Enter the End time : ")
    event=input("Enter the event : ")
    return;
    
def rem_event(date,beg_time):
    date=input("Enter the date : ")
    beg_time=input("Enter the Beginning Time : ")
    return;
    
def upd_event(date,beg_time):
    date=input("Enter the date : ")
    beg_time=input("Enter the Beginning Time : ")
    return;
    
def get_specific(date,beg_time):
    date=input("Enter the date : ")
    beg_time=input("Enter the Beginning Time : ")
    return;
    
def get_range(date):
    date=input("Enter the date : ")
    return;


client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 9995

client_socket.connect((host,port))


user=input("Enter the user name : ")
client_socket.send(user.encode('ascii'))
choice=(input("Enter the functionaly to be done : \n1. Add a new calendar event\n2. Remove a calender event\n3. Update an existing calendar event\n4. Get the event for specific time \n5. Get the events on the specific time range\n"))
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
client_socket.send(date.encode('ascii'))
if(beg_time!=''):
    client_socket.send(beg_time.encode('ascii'))
if(end_time!=''):
    client_socket.send(end_time.encode('ascii'))
if(event!=''):
    client_socket.send(event.encode('ascii'))

client_socket.close()