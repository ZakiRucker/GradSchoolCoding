#import socket
#import sys
from socket import *

#serverName = sys.argv[1]
#serverPort = sys.argv[2]
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("The server is ready to receive")

while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	#if message == "this is a test"
	#	print(and only a test)
	modifiedMessage = ('did it work?')
	print message.decode()
	serverSocket.sendto (modifiedMessage.encode (), clientAddress)
