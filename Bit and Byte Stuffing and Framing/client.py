# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 14:47:54 2019

@author: 17PD04
"""
stri=""
sc=" ESC"
new=""
bini=""
#message=input("Enter the message : ")
message="A ESC B ESC FLAG"
for i in range(len(message)):
    stri+=message[i]
    new+=message[i]
    if(stri.find('ESC')!=-1):
        stri=""
        new+=sc
    if(message[i:]== " FLAG"):
        new+=sc[1:]
        new+=" FLAG"
        break

stri=""
for i in range(len(new)):
    if(new[i]==" "):
        bini+=new[i]
    elif(new[i:i+3]=="ESC"):
        bini+="10100011"
        print(i,i+3)
        i=i+3
    elif(new[i:]=="FLAG"):
        bini+="01111110"
    elif(new[i]!=''):
        temp=bin(ord(new[i]))
        bini+=temp[2:]
     
