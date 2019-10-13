import sys
import socket
import threading
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = (sys.argv[1], int(sys.argv[2]))
print("Starting echo %s port %s" % server_address)
sock.bind(server_address)


# Read in the list of known hosts.
with open('./knownhosts.txt') as fp:
    lines = fp.readlines()

hosts = list()
for line in lines:
    hosts.append(tuple(line.split(' ')))
print(hosts)

# Code that runs in thread to receive messages from other servers
def receive_messages():
    # Bind the socket to a port
    server_address = (sys.argv[1], int(sys.argv[2]))
    print("Starting echo %s port %s" % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    # No listen in UDP
    #sock.listen(1)

    while True:
        # Wait for a connection
        connection, client_address = sock.accept()
        try:

            # Receive the data in small chunks and retransmit it
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            connection.sendall(data)
        finally:
            # Clean up the connection
            connection.close()


# Code that runs in thread to send messages to other servers
def send_peer(host, message):
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock2.connect((host[1], int(host[2])))
    try:
        # Send data
        print('sending {!r}'.format(message))
        hello = b'hello'
        sock2.sendall(hello)

        data = sock2.recv(1024)

        print('Server %s reply: %s' % (host[0], data))
    except:
        print("Connection failed")

    finally:
        sock2.close()



# Code that initates message sending and creates connections to each peer in new threads
def broadcast(message):
    for host in hosts:
        if int(host[2]) != int(sys.argv[2]):
            # Open a connection to each peer in a new thread
            print(host)
            sock.sendto(message, (host[1], int(host[2])))
            #threading.Thread(target = send_peer, args = (host, message)).start()

# The main thread of the program waits for the user to input messages
def listen():
    print("hoee")
    while True:
        print("o")
        #message = input("Enter text: ")
        data, server = sock.recvfrom(1024)
        print("hello")
        print(data.upper())
        print(server)


# Setup the listener thread
threading.Thread(target = listen).start()

time.sleep(5)
broadcast(b'bola')





