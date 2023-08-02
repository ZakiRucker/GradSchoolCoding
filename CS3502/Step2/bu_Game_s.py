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
import queue

RANDOMHIGH = 100
Negative = str('N')
Affirm = str('Y')
q = queue.Queue()
qs = q.qsize()
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
#clientmsg = ''
inviteResponse = ''

# Function definitions

# message
invite = "Would you like to play a guessing game? Y or N\r\n"
waitingMessage = "Waiting for more players to join\r\n"

def leave():
    print (SOLUTION)
    # send finale message to all clients
    for client in clients:
        clientsocket.close()

def broadcast(msg):
    for client in clients:
        client.send(msg.encode())

def scoreboard(clientaddress):
    clients.append(clientaddress)

def dispatch (clientsocket, clientaddress, msg):
    clientsocket.send(msg.encode())

def operator():
    clientmsg = clientsocket.recv(1024)
    clientmsg = clientmsg.decode()
    #print(clientmsg)
    return (clientmsg)

def handleclient(clientsocket, clientaddress):
    clientgreeting = operator()
    dispatch(clientsocket, clientaddress, invite)
    inviteResponse = operator()
    print('inviteResponse within handleclient: %s' % inviteResponse)
    return (inviteResponse)

def invitationProcess(inviteResponse): #errors when enters function
    if inviteResponse == Negative:
        closingMessage = "Goodbye!\r\n"
        clientsocket.send(closingMessage.encode())
        clientsocket.close()
    elif inviteResponse == Affirm:
        t.start()
        q.put(clientaddress)
        print(q)
        print(qs)
        scoreboard(clientaddress)

def playerWait():
    while  qs < 2:    # does not work, try to receive num from array
        dispatch(clientsocket, clientaddress, waitingMessage)
        dispatch(waitingMessage)

def play():
    guessMessage = ("Pick a number between 1 and %s: \r\n" % randomHigh)
    clientsocket.send(guessMessage.encode())
    generatenumber()

    while True:
        guess = clientsocket.recv(1024)
        guessstring = guess.decode()
        print(guessstring)
        # Split the guess string up to get the integer guessed
        guess = int(guessstring.split()[1])
        # Incremenent the counter of the number of guesses
        # If the player has guessed correctly
        if (guess == SOLUTION):
            messagetosend = ("Correct\r\n")
            clientsocket.send(messagetosend.encode())
            running = 0
        else:
            messagetosend = ("Sorry\r\n")
            # Send the response to the player
            clientsocket.send(messagetosend.encode())

            # Close the connection
            clientsocket.close()
            print("Connection closed.")

def generatenumber():
    SOLUTION = random.randrange(1, (GUESS_MAX +1))
    return SOLUTION

while 1:
    (clientsocket, clientaddress) = serversocket.accept()
    t = threading.Timer(game_time, leave)
    print("Connection received from: ", clientaddress)
    print("Connection passed to new thread. Returning to listening.")
    #game = threading.Thread(target = handleclient, args =  (clientsocket, clientaddress)).start()
    invitationProcess(handleclient(clientsocket, clientaddress))
