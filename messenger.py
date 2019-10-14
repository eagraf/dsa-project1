import socket
import threading

class Messenger():

    def __init__(self, host):
        self.send_address = (host['ip_address'], host['udp_start_port'])
        self.recv_address = (host['ip_address'], host['udp_end_port'])

        self.send_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.recv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        self.send_sock.bind(self.send_address)
        self.recv_sock.bind(self.recv_address)

        threading.Thread(target = self.listen).start()

    def send(self, host, message=b"Hello, world"):
        ''' Send a message to another host '''
        self.send_sock.sendto(message, host)

    def listen(self):
        while True:
            data, server = self.recv_sock.recvfrom(1024)
            print(data)
