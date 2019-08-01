# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:06:51 2019

@author: 17pd04
"""
def crc(msg, div, code='000'):
    msg = msg + code
    msg = list(msg)
    div = list(div)

    for i in range(len(msg)-len(code)):
        if msg[i] == '1':
            for j in range(len(div)):
                msg[i+j] = str((int(msg[i+j])+int(div[j]))%2)
    return ''.join(msg[-len(code):])
divisor='10111'
f=open("data.txt",'r')
x=f.read()
y=crc(x,divisor)
if(int(y)==0):
    print("no error")
else:
    print("error")    
    