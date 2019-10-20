import sys
import os
import time
import json
import pickle
import implementation as imp
import event
from messenger import Messenger
from message import Message
from stable_storage import StableStorage
import planes

class Controller:

	def __init__(self):
		self.siteID = sys.argv[1]

		with open('knownhosts.json') as hosts_file:
			self.hosts = json.load(hosts_file)['hosts']

		#self.hostToID = dict()
		count = 0
		for key in sorted(self.hosts.keys()):
			#self.hostToID[key] = count
			self.hosts[key]['id'] = count
			count += 1

		self.messenger = Messenger(self.hosts[self.siteID], self.hosts)
		#self.airport = planes.Planes()

		self.store = StableStorage()

		if len(sys.argv) >= 3:
			handle_test_file()
		else:
			#wu = imp.Wuubern(len(hosts), hostToID[siteID])
			wu, self.airport = self.store.initialize(len(self.hosts), self.hosts[self.siteID]['id'])
			self.messenger.add_listener(wu)
			self.messenger.add_listener(self.store)
			self.messenger.add_listener(self.airport)
			self.handle_user_input(wu)

	#def handle_user_input(wu, messenger, hosts, hostToID, siteID, airport, stable_storage):
	def handle_user_input(self, wu):
		''' Main loop for handling user input. '''
		command = input().split(" ")
		counter = 0
		while command[0] != 'quit':
			if command[0] == "reserve" and len(command) == 3:
				counter += 1

				spotsLeft = self.airport.checkPlanes(command[2], command[1])
				if not spotsLeft:
					print("Cannot schedule reservation for", command[1], ".")
				else:
					plns = command[2].split(',')
					plns = [int(x) for x in plns]
					self.airport.addUser(command[1], self.hosts[self.siteID]['id'], len(self.hosts.keys()), plns)
					ev = event.Event("Reservation", counter, self.hosts[self.siteID]['id'])
					ev.resInfo(command[1], "pending", command[2])
					wu.insert(ev)
					print("Reservation submitted for", command[1], ".")

			elif command[0] == "cancel":
				counter += 1
				for e in wu.dct:
					if(e.resUser == command[1]):
						if e.resStatus == "confirmed":
							plns = e.resPlaneList.split(',')
							plns = [int(x) for x in plns]
							for pln in plns:
								self.airport.removeSpot(pln, e.resUser)
						wu.delete(e)
						break
				print("Reservation for", command[1], "cancelled.")

			elif command[0] == "view":
				for ev in sorted(wu.dct, key=lambda event: event.resUser):
					print(ev.resUser, ev.resPlaneList, ev.resStatus)

			elif command[0] == "log":
				for ev in sorted(wu.log, key=lambda event: event.timeStamp):
					if(ev.type == "insert"):
						print(ev.type, ev.inserted.resUser, ev.inserted.resPlaneList)
					elif(ev.type == "delete"):
						print(ev.type, ev.deleted.resUser)

			elif command[0] == "send":
				np, myMC = wu.send(self.hosts[command[1]]['id'])
				if(len(command) > 2):
					m = Message(np, myMC, self.siteID, command[2])
				else:
					m = Message(np, myMC, self.siteID)

				host = command[1]
				self.messenger.send((self.hosts[host]['ip_address'], self.hosts[host]['udp_end_port']), pickle.dumps(m))

			elif command[0] == "sendall":
				np1 = set()
				for key, host in self.hosts.items():
					if key != self.siteID:
						np, myMC = wu.send(host['id'])
						np1 = np1.union(np)

				m = Message(np1, myMC, self.siteID)

				for key, host in self.hosts.items():
					self.messenger.send((host['ip_address'], host['udp_end_port']), pickle.dumps(m))

			elif command[0] == "clock":
				for i in range(len(wu.myMC)):
					for j in range(len(wu.myMC[i]) -1):
						print(wu.myMC[i][j], end = " ")
					print(wu.myMC[i][-1])
			else:
				print("invalid command")
			
			#  Write to stable storage
			self.store.store()

			# Wait for next command
			command = input().split(" ")

		print("exiting...")
		os._exit(0)


def handle_test_file():
	''' Execute a sequence of commands with timings rather than taking user input. '''
	print("Handling test file")

if __name__== "__main__":
	controller = Controller()