import socket
import pickle
import threading

class Messenger:

    def __init__(self, host, hosts):
        self.send_address = (host['ip_address'], host['udp_start_port'])
        self.recv_address = (host['ip_address'], host['udp_end_port'])

        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.send_sock.bind(self.send_address)
        self.recv_sock.bind(self.recv_address)

        self.listeners = list()
        self.hosts = hosts

        threading.Thread(target = self.listen).start()

    def add_listener(self, listener):
        self.listeners.append(listener)

    def send(self, host, message=b"Hello, world"):
        ''' Send a message to another host '''
        self.send_sock.sendto(message, host)

    def listen(self):
        while True:
            data, server = self.recv_sock.recvfrom(1024)
            message = pickle.loads(data)
            #print(message.message)
            pID = self.hosts[message.siteID]['id']

            #for listener in self.listeners:
            self.listeners[0].receive(message.clock, pID, message.np) 
            self.listeners[1].receive(message.clock, pID, message.np)
            
            users, myID, userPlanes = self.listeners[0].getUsers(message.np)
            self.listeners[2].receiveAdd(users, myID, len(self.hosts), userPlanes)
            self.listeners[2].receive(pID, self.listeners[0])
