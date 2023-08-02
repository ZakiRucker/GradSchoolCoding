from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', 12000))

while True:
	print("The server is ready to receive")
	message, clientAddress = serverSocket.recvfrom(2048)
	print message.decode()
	
	modifiedMessage = ('did it work?')
	print modifiedMessage
	serverSocket.sendto (modifiedMessage.encode (), clientAddress)
	
	while True:
		response, clientAddress = serverSocket.recvfrom(2048)
		print response.decode()
	
		finalResponse = ('Congrats!!!')
		print finalResponse
		serverSocket.sendto (finalResponse.encode (), clientAddress)
		
	break
