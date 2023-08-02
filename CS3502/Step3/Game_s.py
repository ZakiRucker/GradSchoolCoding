'''
Created by: Rucker, Zaki
CS3502
Feb 2018
'''
# second client is not linking into the game
# game is not printing Correct or not, until the second game is played

import sys
import random
import socket
import threading
import signal
import time

global numbertoguess, clients, guessstring, t, sock, guess, numbertoguess
clients = {}
guessstring = 0
t = 0
sock = 0

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
    #while True:
    # Receive the client's greeting
    clientgreeting = clientsocket.recv(1024).decode()
    # Send the welcome message to the client
    welcomemessage = "Greetings\r\n"
    clientsocket.send(welcomemessage.encode('ascii'))             

# game loop
def game(clientsocket, clientaddress):
    while True:
        #threading.Timer(game_time, leave(numbertoguess)).start()
        #guess = clientsocket.recv(1024)
        guessstring = clientsocket.recv(1024).decode('ascii')
        sock = clientsocket
        print(guessstring)
        # Split the guess string up to get the integer guessed
        guess = int(guessstring.split()[1])
        clients[sock][1] = guess
         
def expire():
    sock = clientsocket
    guess = clients[sock][1]
    for sock, guessstring in clients.items():
        #print(clients[sock][1])
        numbertoguess = generatenumber()
        reply = ("Your number was %s.\r\n" % clients[sock][1])
        #guess = int(guess)
        if (guess == numbertoguess):
            messagetosend = ("%s\r\n Correct\r\n" % reply)
            clientsocket.send(messagetosend.encode('ascii'))
        else:
            # Calculate how far the player was away from the actual number
            difference = abs(guess - numbertoguess)
            if difference < 2:
                messagetosend = ("You were close\r\n %s The answer was %s \r\n" % (reply, numbertoguess))
            else:
                messagetosend = ("\rSorry,the number was %s. %s" % (numbertoguess, reply))
            # Send the response to the player  
            clientsocket.send(messagetosend.encode('ascii'))
    clients[sock][1] = 0
    
    # Close the connection
    #clientsocket.close()
    #print("Connection closed.")
    #return numbertoguess

def leave(numbertoguess):
    game_end = "The number was %s." % numbertoguess
    clientsocket.send(game_end.encode())
    clientsocket.close()

def generatenumber():
	return random.randrange(1, 101)

# Main server loop

while 1:
    clientsocket, clientaddress = serversocket.accept()
    sock = clientsocket
    clients[sock] =  [clientaddress, guessstring, t]
    print("Connection received from: ", clientaddress)
    print("Connection passed to new thread. Returning to listening.")
    t = threading.Thread(target = handleclient, args =  (clientsocket, clientaddress))
    t.start()
    gtimer = threading.Timer(int(game_time), game, (clientsocket, clientaddress))
    gtimer.start()
    #e = threading.Thread(target = expire, args = (guess, numbertoguess))
    #e.start()
    expire()
