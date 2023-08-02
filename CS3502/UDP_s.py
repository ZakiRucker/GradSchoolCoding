from socket import *
import sys
import select

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))
print("The server is listening")

while (1):
	message, clientAddress = serverSocket.recvfrom(2048)
	
	if message == "When you pay off the first baseman every month, who gets the money?" :
		print("received: %s" % message)
		myResponse = 'Every dollar of it. And why not, the man\'s entitled to it.'
		print ("sending: %s" % myResponse)
		serverSocket.sendto (myResponse.encode(), clientAddress)

	elif message == "Who is?" :
		print("received: %s" % message)
		lastWord = 'Yes'
		print ("sending: %s" % lastWord)
		serverSocket.sendto (lastWord.encode(), clientAddress) 
