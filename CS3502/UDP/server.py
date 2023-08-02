# CS 3502
# Network programming
# by: Rucker, Zaki
#
# Server side 
#

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if len(sys.argv) < 3:
    print ("Need to provide <hostname>, e.g., localhost and port number in the command line!")
    exit(1)
    
# Bind the socket to the address given on the command line
server_name = sys.argv[1]
server_port = sys.argv[2]
server_address = (server_name, server_port)
print("starting up on %s port %s" % server_address)
sock.bind(server_port)
#sock.listen(1)

while True:
    print("waiting for a connection")
    connection, client_address = sock.accept()
    try:
        print("client connected:", client_address)
        while True:
            data = connection.recv(250) #250 characters at a time
            print("received %s" % data)
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
