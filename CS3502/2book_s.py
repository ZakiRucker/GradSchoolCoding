from socket import *
import sys
import select

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

while (1):
	print("The server is listening")
	message, clientAddress = serverSocket.recvfrom(2048)
	print message.decode()
	
	if message == "When you pay off the first baseman every month, who gets the money?" :
		myResponse = 'Every dollar of it. And why not, the man\'s entitled to it.'
		print 'me:', myResponse
		serverSocket.sendto (myResponse.encode(), clientAddress)
	elif message == "Who is?" :
		lastWord = 'Yes'
		print 'me:',lastWord
		serverSocket.sendto (lastWord.encode(), clientAddress) 
