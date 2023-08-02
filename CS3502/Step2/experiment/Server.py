from socket import *
import random
import argparse as argp
import threading
import time

global num
#x = True

#Setup IP, Port, and Game Time arguments
args = argp.ArgumentParser(usage="program [ip_address] [port_number] [game_time]")
args.add_argument("ip_address", help="ip address to use", type=str) #adds ip address arg
args.add_argument("port_number", help="port number to use", type=int) #adds port number arg
args.add_argument("game_time", help="time in seconds for game", type=int) #adds game time arg
inpt=args.parse_args()
ip=inpt.ip_address
port=inpt.port_number
gt=inpt.game_time
socket_list = {}

#Setup Server Socket
serversocket = socket(AF_INET, SOCK_STREAM )
serversocket.bind((ip, port))
serversocket.listen(5)
print( "The server is ready to receive\n" )

#Function asks for number and returns value to player
def handleclient(clientsocket,addr):
    #while True:
    guess = ("Please guess a number between 1 and 100: ")
    clientsocket.send(guess.encode())
    while True:
        try:
            clientsend = clientsocket.recv(1024).decode()
            socket_list[clientsocket] = clientsend #key is socket, value is clientsend
            guess_reply = ("Your guess was %s.\n" % (clientsend))
            clientsocket.send(guess_reply.encode())
        except:
            break

#Function sets 
def expire(socket_list, addr):
    global x
    global num
    for clientsocket,clientnum in socket_list.items():
        clientnum = int(clientnum)
        if (clientnum == number):
            response = ("Correct, please play again soon!\r\n")
            clientsocket.send(response.encode())
        else:
            response = ("Sorry, the number was %d and your final guess was %d.\r\n" % (number, clientnum))
            clientsocket.send(response.encode())
        close_response=("The game timer expired, closing connection\n")
        clientsocket.send(close_response.encode())
        timer.cancel()
        print("Game timer expired for client %s:%d: Connection closed..." % (addr[0],addr[1]))
        clientsocket.close()
        x = False #reset global x and start new instance of the game.
        num = 0
    #serversocket.close()
    socket_list.clear()
    return

if __name__ == "__main__":
    running = 1
    global x
    num = 0
    while 1:
        number = random.randint(1, 100)
        x = True
        #print(number)
        while x == True:
            clientsocket, addr = serversocket.accept()
            socket_list[clientsocket] = 0
            print("Connection received from: ", addr)
            t = threading.Thread(target=handleclient, args=(clientsocket, addr))
            t.start()
            num += 1
            print("# of clients: %d" %num)
            if num > 1:
                timer = threading.Timer(gt, expire, args=(socket_list, addr) )
                timer.start()
            print(threading.active_count())
            print("Connection passed to new thread. Returning to listening.")
