from socket import *

serverName = 'localhost'
serverPort = 10000
ClientSocket = socket(AF_INET,SOCK_DGRAM)

try:
    #print("Sending first message")
    message = ("Ha! Drunk piano player...you're so drunk you can't hit nothing.\n"
           "In fact - you're probably seeing double!\n")
    message1 = ("Noooooo!!!")
    ClientSocket.sendto(message.encode(), (serverName, serverPort))
    ClientSocket.sendto(message1.encode(), (serverName, serverPort))
    serverReply, serverAddress = ClientSocket.recvfrom(2048)
    print(serverReply.decode())

finally:
    ClientSocket.close()