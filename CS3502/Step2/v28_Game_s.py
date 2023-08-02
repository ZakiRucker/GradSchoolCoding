#####################################################################################
#
# Created by: Rucker, Zaki
# CS3502
# Feb 2018
#
#####################################################################################

# import statements

import sys
import random
import socket
import threading
import signal

RANDOMHIGH = 20
Negative = str('N')
Affirm = str('Y')

clients = []

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
#clients.append(client(addr, sock, len(clients)))     client not defined

how_many = threading.active_count()

# array to add clients as they agree to play
clients = []


# Function definitions

def broadcast(msg):
	for client in clients:
		client.send(msg.encode())


def handleclient(clientsocket, clientaddress):
	clientgreeting = clientsocket.recv(1024)
	invite = "Would you like to play a guessing game? Y or N\r\n"
	clientsocket.send(invite.encode('ascii'))
	inviteResponse = clientsocket.recv(1024)
	inviteResponse = inviteResponse.decode('ascii')
	#print(inviteResponse)

	
	if inviteResponse == Negative:
		closingMessage = "Goodbye!\r\n"
		clientsocket.send(closingMessage.encode('ascii'))
		clientsocket.close()

	elif inviteResponse == Affirm:
		while how_many < 2:    # does not work, need to receive num from array
			waitingMessage = "Waiting for more players to join\r\n"
			clientsocket.send(waitingMessage.encode('ascii'))
		
	
		# Send the welcome message to the client
		guessMessage = ("Pick a number between 1 and %s: \r\n" % randomHigh)
		clientsocket.send(guessMessage.encode('ascii'))


#moved here
		# Main loop

		running = 1

		while running:

			guess = clientsocket.recv(1024)
			guessstring = guess.decode('ascii')
			print(guessstring)
			# Split the guess string up to get the integer guessed
			guess = int(guessstring.split()[1])
			# Incremenent the counter of the number of guesses
			numberofguesses += 1
			running = 1
			# If the player has guessed correctly
			if (guess == numbertoguess):
				messagetosend = ("Correct\r\n")
				clientsocket.send(messagetosend.encode('ascii'))
				running = 0
			else:
				messagetosend = ("Sorry\r\n")
				# Send the response to the player
				clientsocket.send(messagetosend.encode('ascii'))
		

		# Close the connection
			clientsocket.close()
			print("Connection closed.")

def generatenumber():
    SOLUTION = random.randrange(1, (GUESS_MAX +1))
    return SOLUTION

# Main server loop

while 1:
	(clientsocket, clientaddress) = serversocket.accept()
	print("Connection received from: ", clientaddress)
	threading.Thread(target = handleclient, args =  (clientsocket, clientaddress)).start()
	print("Connection passed to new thread. Returning to listening.")
