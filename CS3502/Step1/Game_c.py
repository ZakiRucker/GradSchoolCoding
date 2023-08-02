'''
Created by: Rucker, Zaki
CS3502
Feb 2018
'''

import socket
import sys
import threading

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
# Wait for a response, then print said response to the console
response = clientsocket.recv(1024)
print(response.decode('ascii'))

while True:
	# Ask for user to guess a number
	#threading.Thread(target = operator, args = ()).start()
	guess = input("Pick a number from 1 to 100: ")
	# Format the guess, ready to send to the server
	guessstring = "Guess: " + str(guess) + "\r\n"
	clientsocket.send(guessstring.encode('ascii'))
	response = clientsocket.recv(1024).decode('ascii')
	print (response)


	# Determine if the game is over
	if (response == "Correct\r\n"):
		running = 0

clientsocket.close()
