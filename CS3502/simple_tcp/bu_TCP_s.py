from socket import *
#import socket
import sys

# Create a TCP/IP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

if len(sys.argv) < 2:
    	print ("Need to provide <hostname>, e.g., localhost in the command line!")
    	exit(1)
    
# Bind the socket to the address given on the command line
server_name = sys.argv[1]
serverPort = (12000)
#print("starting up on %s port %s" % server_address)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

while True:
    	sock, addr = serverSocket.accept()
	sentence = sock.recv(1024).decode()
	print("received: %s" % sentence)
	
	response = 'Yeah, it could be.'
	print("sending: %s" % response)
	sock.sendall(response)

	reply = sock.recv(1024).decode()
	print("received: %s" % reply)

	finalWord = 'Because.'
	print("sending: %s" % finalWord)
	sock.sendall(finalWord)

	sock.close()

#        	print("client connected:", client_address)
#        	while True:
#            		message = connection.recv(2048) 
#            		print("received: %s" % message)
#            		if message == "I throw the ball to first base, whoever it is grabs the ball, so the guy runs to second. Who picks up the ball and throws it to what. What throws it to I don't know. I don't know throws it back to tomorrow--a triple play." :
#				response = 'Yeah, it could be.'
#				print ("sending: %s" % response)
#                		connection.sendall(response)
#				
#			elif message == "Another guy gets up and it's a long ball to center." :
#				response2 = 'Because.'
#				print ("sending: %s" % response2)
#				connection.sendall(response2)
#            	else:
#                	break
#    	finally:
#	        connection.close()
