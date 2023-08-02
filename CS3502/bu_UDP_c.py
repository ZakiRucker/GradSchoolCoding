#import socket
#import sys
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = 'When you pay off the first baseman every month, who gets the money?'
print ("seding: %s" % message)
clientSocket.sendto (message.encode(),(serverName,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("received: %s" % modifiedMessage)

response = 'Who is?'
print ("sending: %s" % response)
clientSocket.sendto (response.encode(),(serverName,serverPort))

finalMessage, serverAddress = clientSocket.recvfrom(2048)
print("received: %s" % finalMessage)

#clientSocket.close()
