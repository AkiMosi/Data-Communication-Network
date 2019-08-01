# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
f=open("data.txt",'w')
divisor = '10111'
input_string = input("Enter the message : ")
data = (''.join(format(ord(x), 'o') for x in input_string)) 
print (data)
print(len(data))
x=crc(data,divisor,(len(divisor)-1)*'0')
data1=data+x
f.write(data1)
f.close()

