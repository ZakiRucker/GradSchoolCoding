
from socket import *

# Create a TCP/IP socket


# Bind the socket to the address given on the command line
server_name = '127.0.0.1'
serverPort = 10000
sock = socket(AF_INET, SOCK_STREAM)
sock.bind((server_name, serverPort))
sock.listen(1)
print("The server is ready to receive\n")

while True:
    connection, addr = sock.accept()
    data = connection.recv(1024).decode()
    if data:
        print("Connection received\n")
        print(data+"\n")
        message = ("Ha! Drunk piano player...you're so drunk you can't hit nothing.\n")
        message1 = ("In fact - you're probably seeing double!\n")
        message2 = ("Noooo!\n")
        connection.send(message.encode())
        connection.send(message1.encode())
        connection.send(message2.encode())
        print("Sent response\n")
        connection.close()
    else:
        break

connection.close()