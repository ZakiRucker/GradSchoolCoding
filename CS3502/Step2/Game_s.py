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
SOLUTION = 0
Negative = str('N')
Affirm = str('Y')
q = queue.Queue()
qs = q.qsize()
global status
clients = []
whereTo = ''
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

# array to add clients as they agree to play
clients = []


# Function definitions

# message
invite = "Would you like to play a guessing game? (Y or N)  "
waitingMessage = "Waiting for more players to join\r\n"
winner = "Correct\r\n"
loser = "Sorry\r\n"
bye = "Goodbye\r\n"

'''def join():
    whereTo = (clientsocket, clientaddress)
    return ((clientsocket, clientaddress)) '''

def leave():
    ''' dispatches final messages and closes client connections.'''
    print (SOLUTION)
    # send finale message to all clients
    for client in clients:
        clientsocket.close()

def broadcast(msg):
    '''Intend to use to send a message to all clients.'''
    for client in clients:
        client.send(msg.encode())

def scoreboard(clientsocket):
    ''' adds clients to the list to control communications and messaging.'''
    clients.append(clientsocket)

def dispatch (clientsocket, clientaddress, msg):
    '''sends server messages to the clients.'''
    clientsocket.send(msg.encode())

def operator():
    '''receives messages from the client and returns them to the calling function.'''
    clientmsg = clientsocket.recv(1024)
    clientmsg = clientmsg.decode()
    if clientmsg == 'Hello Server':
        pass
    return (clientmsg)

''' try code without the invitation
def handleclient(clientsocket, clientaddress):
    clientgreeting = operator()  # recv greeting
    dispatch(clientsocket, clientaddress, invite)   # send invit to client
    inviteResponse = operator()      # recv client response to invitation
    print(inviteResponse)
    return (inviteResponse)      # return inviteResponse to calling function

def invitationProcess(inviteResponse): #Does not process 'N'
    if inviteResponse == Negative:
        dispatch(bye)
        clientsocket.send(closingMessage.encode())
        clientsocket.close()
    elif inviteResponse == Affirm:
        t.start()
        q.put(clientsocket, clientaddress)
        print(q)
        print(qs)
        scoreboard(clientaddress)  '''

def playerWait(clientsocket, clientaddress):
    ''' block clients until we have enough players.'''
    dispatch(clientsocket, clientaddress, waitingMessage)

def play(clientsocket):
    ''' where the magic happens, send game question and process answer.'''
    t.start()
    '''q.put(clientsocket, clientaddress)
    print(q)
    print(qs)'''
    scoreboard(clientsocket)
    guessMessage = ("Pick a number between 1 and %s: \r\n" % RANDOMHIGH)
    clientsocket.send(guessMessage.encode())
    generatenumber()

    while True:
        guess = operator()
        print(guess)
        # If the player has guessed correctly
        if (guess == SOLUTION):
            dispatch (winner)
        else:
            dispatch(clientsocket, clientaddress, loser)
            leave()
            print("Connection closed.")

def generatenumber():
    ''' generate the random number.'''
    SOLUTION = random.randrange(1, (RANDOMHIGH+1))
    return SOLUTION

while True:
    ''' main.'''
    PLAYERS = 0
    clientsocket, clientaddress = serversocket.accept()
    clients[int(clientsocket)] = 0
    print("Connection received from: ", clientaddress)
    print("Connection passed to new thread. Returning to listening.")
    pw = threading.Thread(target = playerWait, args=(clientsocket, clientaddress))
    pw.start()
    PLAYERS += 1
    t = threading.Timer(int(game_time), leave)
    playerWait(clientsocket, clientaddress)
    if PLAYERS >= 1:
        play(clientsocket)
    
