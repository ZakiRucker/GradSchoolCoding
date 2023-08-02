
from socket import *

#Create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)

#Bind the socket to the port
server_address = ('localhost', 10000)
print("Start using %", server_address)
sock.bind(server_address)

while True:
    print("\nWaiting to receive data")
    data, address = sock.recvfrom(1024)
    if data:
        print("Connection received\n")
        print(data.decode())
        message = ("I have two barrels!\nOne for each of you!!\n")
        send = sock.sendto(message.encode(), address)
        print("Sent response\n")
    else:
        break
