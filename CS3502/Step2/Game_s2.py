##################################
#
# Created by: Rucker, Zaki
# CS3502
# Game Server
#
##################################

import sys
import random
import socket
import threading
import signal
import string

GUESS_MAX = 100

SOLUTION = 0
incomingmsg = ''


#Get command line args
if len(sys.argv) < 4:
    print('Please input in the following format: host, port, and game time.')
    exit(1)
host = socket.gethostbyname(sys.argv[1])
port = sys.argv[2]
game_time = sys.argv[3]


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind((host, int(port)))
serversocket.listen(5)
print('Server %s is listening on port %s.' % (host,port))

def newClient(clientaddress, clientsocket):
    print('Connection received from: %s.' % clientaddress)

def dispatch(msg):
    #outgoingmsg = msg.encode()
    clientsocket.send(msg.encode())

def operator():
    incomingmsg = clientsocket.recv(1024).decode()
    print(incomingmsg)
    check_response(incomingmsg)

def check_response(incomingmsg):
    if incomingmsg == 'Y':
        game()
    elif incomingmsg == 'N':
        leave()
    elif incomingmsg.isalnum:
        if incomingmsg == SOLUTION:
            dispatch(correct)
            dispatch(over)
            leave()
        else:
            dispatch(wrong)
            dispatch(over)
            leave()

def game():
    SOLUTION = random.randrange(1, (GUESS_MAX + 1))
    print(SOLUTION)
    dispatch(guess)
    PLAYER_GUESS = operator()
    print(PLAYER_GUESS)
    print(PLAYER_GUESS == SOLUTION)

def leave():
    print (SOLUTION)
    dispatch(bye)
    clientsocket.close()

#messages
invitation = ("Would you like to play a guessing game? (Y of N) ")
wait = ("Wainting for more players to join.")
bye = ("Goodbye!")
guess = ("Pick a number between 1 and %s: "   % GUESS_MAX)
correct = ("Correct!\r\n You WIN!!!")
wrong = ("Sorry, you lose. The number was %s\r\n" % SOLUTION)
over = ("Game Over, Reconnect to play again.\r\n")


while 1:
    (clientsocket, clientaddress) = serversocket.accept()
    join = threading.Thread(target = newClient, args = (clientsocket, clientaddress))
    join.start()
    #receiving = threading.Thread(target = operator, args = ())
    #receiving.start()
    dispatch(invitation)
    operator()
    check_response(incomingmsg)
    
    if incomingmsg == 'N':
        pass #leave function once comparrison works

