######################################################
######################################################
#
# Created by: Rucker, Zaki
# CS3502
# Feb 2018
#
######################################################
######################################################

import sys
import random
import socket
import threading
import signal

randomhigh = 100

# Get command line arguments

if len(sys.argv) < 4:
	print('Please input in the following format: host, port, and game time.')
	exit(1)
host = socket.gethostbyname('localhost')
port = sys.argv[2]
game_time = sys.argv[3]


# Set up the socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, int(port)))
serversocket.listen(5)
print('Server %s is listening on port %s.' % (host, port))

# Function definitions

def handleclient(clientsocket, clientaddress):
	clientgreeting = clientsocket.recv(1024)  # recv client greeting
	welcomemessage = "Greetings\r\n"
	clientsocket.send(welcomemessage.encode('ascii')) # send greeting to client

	running = 1
	# Generate a random number for the client to try and guess
	numbertoguess = generatenumber()

	# Main loop
	while running:

		guess = clientsocket.recv(1024)
		guessstring = guess.decode('ascii')
		print(guessstring)
		# Split the guess string up to get the integer guessed
		guess = int(guessstring.split()[1])
		running = 1
		# If the player has guessed correctly
		if (guess == numbertoguess):
			messagetosend = ("Correct\r\n")
			clientsocket.send(messagetosend.encode('ascii'))
			running = 0
		else:
			# Calculate how far the player was away from the actual number
			difference = abs(guess - numbertoguess)
			if difference < 4:
				messagetosend = ("Close\r\n")
			else:
				messagetosend = ("Far\r\n")
			# Send the response to the player
			clientsocket.send(messagetosend.encode('ascii'))
	# Close the connection
	clientsocket.close()
	print("Connection closed.")

def generatenumber():
	return random.randrange(1, randomhigh + 1)

# Main server loop

while 1:
	(clientsocket, clientaddress) = serversocket.accept()
	print("Connection received from: ", clientaddress)
	print("Connection passed to new thread. Returning to listening.")
	threading.Thread(target = handleclient, args =  (clientsocket, clientaddress)
