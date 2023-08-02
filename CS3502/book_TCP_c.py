from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

message = ('line one')
print("sending: %s" % message)
clientSocket.send(message.encode())

reply = clientSocket.recv(1024)
print ('received:',reply.decode())

myResponse = ('line three')
print("sending: %s" % myResponse)
clientSocket.send(myResponse.encode())

finalWord = clientSocket.recv(1024)
print ("received: %s" %finalWord)

clientSocket.close()
