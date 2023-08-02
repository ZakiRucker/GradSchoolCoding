'''
Created by: Rucker, Zaki
CS3502
Feb 2018
'''

import sys
import random
import socket
import threading
import signal
import time

global numbertoguess

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
    while True:
        # Receive the client's greeting
        clientgreeting = clientsocket.recv(1024)
        # Send the welcome message to the client
        welcomemessage = "Greetings\r\n"
        clientsocket.send(welcomemessage.encode('ascii'))             
        # Send client game_time
        #int(game_time)
        #clientsocket.send(game_time.encode())

        running = 1
        numberofguesses = 0
        # Generate a random number for the client to try and guess

        # Main loop
        while running:
            numbertoguess = generatenumber()
            #threading.Timer(game_time, leave(numbertoguess)).start()
            guess = clientsocket.recv(1024)
            guessstring = guess.decode('ascii')
            print(guessstring)
            # Split the guess string up to get the integer guessed
            guess = int(guessstring.split()[1])
            # Incremenent the counter of the number of guesses
            numberofguesses += 1
            running = 1
            # If the player has guessed correctly
            time.sleep(int(game_time)) 
            if (guess == numbertoguess):
                messagetosend = ("Correct\r\n")
                clientsocket.send(messagetosend.encode('ascii'))
                running = 0
            else:
                # Calculate how far the player was away from the actual number
                difference = abs(guess - numbertoguess)
                if difference < 2:
                    messagetosend = ("Close\r\n")
                else:
                    messagetosend = ("\rSorry, you lose. The number was %s.\n" % numbertoguess)
                # Send the response to the player
                clientsocket.send(messagetosend.encode('ascii'))
    # Close the connection
    clientsocket.close()
    print("Connection closed.")
    return numbertoguess

def leave(numbertoguess):
    game_end = "The number was %s." % numbertoguess
    clientsocket.send(game_end.encode())
    clientsocket.close()

def generatenumber():
	return random.randrange(1, 101)

# Main server loop

while 1:
    (clientsocket, clientaddress) = serversocket.accept()
    print("Connection received from: ", clientaddress)
    threading.Thread(target = handleclient, args =  (clientsocket, clientaddress)).start()
    print("Connection passed to new thread. Returning to listening.")
