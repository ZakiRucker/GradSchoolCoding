from socket import *
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) < 2:
    	print ("Need to provide <hostname>, e.g., localhost in the command line!")
    	exit(1)

# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], 12000)
print("connecting to %s port %s" % server_address)
sock.connect(server_address)

message = "I throw the ball to first base, whoever it is grabs the ball, so the guy runs to second. Who picks up the ball and throws it to what. What throws it to I don't know. I don't know throws it back to tomorrow--a triple play."
print("sending: %s" % message)
sock.sendall(message)

reply = sock.recv(1024).decode()
print("received: %s" % reply)

response = ('Another guy gets up and it\'s a long ball to center.')
print("sending: %s" % response)
sock.sendall(response.encode())

finalWord = sock.recv(1024).decode()
print("received: %s" % finalWord)

sock.close()
