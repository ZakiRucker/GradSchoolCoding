from socket import *
import time
from types import *

def recv(addr,port):
    msg=""
    csock = socket(AF_INET,SOCK_STREAM)
    csock.connect((addr,port))
    quote = ("I have two guns.")
    quote1 = ("\nOne for each of you.")
    csock.send(quote.encode())
    csock.send(quote1.encode())
    while True:
        data = csock.recv(4086)
        if data:
            msg+=data.decode()
            #return(msg)
        else:
            csock.close()
            return(msg)

#Create TCP/IP Socket:
#server_address = ('127.0.0.1', 10000)
addr='127.0.0.1'
port=10000
print("Connecting to %s port %s\n" % (addr,port))
msg=recv(addr,port)
print(msg)
print("Success")

