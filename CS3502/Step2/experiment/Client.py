from socket import *
import argparse as argp
from ipaddress import ip_address
import threading
import os

args = argp.ArgumentParser(usage="program [ip_address] [port_number]")
args.add_argument("ip_address", help="ip address to use", type=str) #adds ip address arg
args.add_argument("port_number", help="port number to use", type=int) #adds port number arg
inpt=args.parse_args()
ip=inpt.ip_address
port=inpt.port_number
#print(port)# Set up the socket
reply = ""
clientsocket = socket(AF_INET, SOCK_STREAM)

def receive_thread(clientsocket):
    global reply
    while True:
        reply = clientsocket.recv(1024).decode()
        if ("expired" in reply):
            print(reply)
            running = 0
            clientsocket.close()
            os._exit(0)
        else:
            print(reply)

try:
    clientsocket.connect((ip, port))
except ConnectionRefusedError:
    print("The connection was refused")
    exit(0)
print("Connected")
running = 1


while running:
    receiver = threading.Thread(target=receive_thread, args=[clientsocket])
    receiver.start()
    my_guess = input()
    clientsocket.send(my_guess.encode())

