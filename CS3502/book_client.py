#import socket
#import sys
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = 'When you pay off the first baseman every month, who gets the money?'
print 'me:',message
clientSocket.sendto (message.encode(),(serverName,serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())

response = 'Who is?'
print 'me:',response
clientSocket.sendto (response.encode(),(serverName,serverPort))

finalMessage, serverAddress = clientSocket.recvfrom(2048)
print(finalMessage.decode())

#clientSocket.close()
