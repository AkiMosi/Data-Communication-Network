import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=9995

client_socket.connect((host,port))


databits=input("Enter the code : ")
m=len(databits)
r=0
    
while(True):
    if(2**r>=m+r+1):
        break
    else:
        r+=1

print("The length of data words : ",m)
print("The length of the parity bits : ",r)

codelen=r+m

code=[]
j=0
index=0

for i in range(1,codelen+1):
    if(i==2**j):
        code.append("*")
        j+=1
    else:
        code.append(databits[index])
        index+=1

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
    code[(2**i)-1]=str(parbit.__and__(1))
  
databits=''
for i in range(codelen):
    databits+=code[i]
print(databits)
client_socket.send(str(r).encode('ascii'))
client_socket.send(str(databits).encode('ascii'))
client_socket.close()
