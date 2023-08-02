###################################################################
#
# Created by: Rucker, Zaki
# CS3502
# Feb 2018
#
###################################################################

import socket
import sys

#Get command line arguments
if len(sys.argv) < 3:
	print('Please input in the format: host and port')
	exit(1)

host = sys.argv[1]
port = sys.argv[2]

print ("Connecting to server...")

# Set up the socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
try:
	clientsocket.connect((host, int(port)))
except ConnectionRefusedError:
	print ("The connection was refused.")
	exit(0)
print("connected!\n")


# Send the greeting message to the server

message = "Hello\r\n"
clientsocket.send(message.encode('ascii'))


# Receive game invitation

invitation = clientsocket.recv(1024)
invitationstring = invitation.decode('ascii')

# Send inviteResponse

inviteResponse = input(str(invitationstring))
clientsocket.send(inviteResponse.encode('ascii'))


# Waiting for enough players to start

# game start

# receive question/send guess
guessMessage = clientsocket.recv(1024)
guessMessagestring = guessMessage.decode('ascii')
myNum = input(str(guessMessagestring))
clientsocket.send(myNum.encode('ascii'))

#running = clientsocket.recv(1024)

while running:
	#game_time = clientsocket.recv(1024)
	#print(game_time.decode())
	# Ask for user to guess a number
	#guess = input("Enter your guess: ")
	# Format the guess, ready to send to the server
	#guessstring = "Guess: " + str(guess) + "\r\n"
	# Send the guess
	clientsocket.send(guessstring.encode('ascii'))

	# Wait for the response from the server
	response = clientsocket.recv(1024).decode('ascii')
	print (response)
	

	# Determine if the game is over
	if (response == "Correct\r\n"):
		running = 0

clientsocket.close()
