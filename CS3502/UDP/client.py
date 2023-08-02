# CS 3502
# Networking programming
# by: Rucker, Zaki 
#
# Client side
#

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if len(sys.argv) < 3:
    print ("Need to provide <hostname>, e.g., localhost and port number in the command line!")
    exit(1)

# Connect the socket to the port on the server given by the caller
server_port = sys.argv[2]
server_address = (sys.argv[1], server_port)
print("connecting to %s port %s" % server_address)
sock.connect(server_address)

try:
    
    message = b"This is the message.  It will be repeated multiple times."
    print("sending %s" % message)
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(250)
        amount_received += len(data)
        print("received %s" % data)

finally:
    sock.close()
