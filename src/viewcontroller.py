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

def main():
	siteID = sys.argv[1]

	with open('knownhosts.json') as hosts_file:
		hosts = json.load(hosts_file)['hosts']

	hostToID = dict()
	count = 0
	for key in sorted(hosts.keys()):
		hostToID[key] = count
		hosts[key]['id'] = count
		count += 1
	
	users = dict()
	messenger = Messenger(hosts[siteID], hosts)
	airport = planes.Planes()

	store = StableStorage()

	if len(sys.argv) >= 3:
		handle_test_file()
	else:
		#wu = imp.Wuubern(len(hosts), hostToID[siteID])
		wu = store.initialize(len(hosts), hostToID[siteID])
		messenger.add_listener(wu)
		messenger.add_listener(store)
		handle_user_input(wu, messenger, hosts, hostToID, siteID, airport, store)


def read_stable_storage():
	''' If a stable storage file was written in this directory, read it to load dictionary '''
	pass

def handle_user_input(wu, messenger, hosts, hostToID, siteID, airport, stable_storage):
	''' Main loop for handling user input. '''
	command = input().split(" ")
	counter = 0
	while command[0] != 'quit':
		if command[0] == "reserve":
			counter += 1

			spotsLeft = airport.checkPlanes(command[2])
			if not spotsLeft:
				print("Cannot schedule reservation for", command[1])
				continue

			ev = event.Event("Reservation", counter, hostToID[siteID])
			ev.resInfo(command[1], "pending", command[2])
			wu.insert(ev)
			print("Reservation submitted for", command[1])

		elif command[0] == "cancel":
			counter += 1
			for e in wu.dct:
				if(e.resUser == command[1]):
					if e.resStatus == "confirmed":
						plns = e.resPlaneList.split(',')
						plns = [int(x) for x in plns]
						for pln in plns:
							airport.removeSpot(pln, e.resUser)
					wu.delete(ev)
					break
			print("Reservation for", command[1], "canceled")

		elif command[0] == "view":
			for ev in sorted(wu.dct, key=lambda event: event.resUser):
				print(ev.resUser , ev.resPlaneList, ev.resStatus)
			#print("view command received")

		elif command[0] == "log":
			for ev in sorted(wu.log, key=lambda event: event.timeStamp):
				if(ev.type == "insert"):
					print(ev.type, ev.inserted.resUser, ev.inserted.resPlaneList)
				elif(ev.type == "delete"):
					print(ev.type, ev.deleted.resUser)
			#print("log command received")

		elif command[0] == "send":
			np, myMC = wu.send(hostToID[command[1]])
			if(len(command) > 2):
				m = Message(np, myMC, command[2])
			else:
				m = Message(np, myMC)

			host = command[1]
			messenger.send((hosts[host]['ip_address'], hosts[host]['udp_end_port']), pickle.dumps(m))

		elif command[0] == "sendall":
			for host in hosts.values():
				np, myMC = wu.send(host['id'])
				m = Message(np, myMC)
				messenger.send((host['ip_address'], host['udp_end_port']), pickle.dumps(m))

		elif command[0] == "clock":
			#print("clock command received")
			for i in range(len(wu.myMC)):
				for j in range(len(wu.myMC[i]) -1):
					print(wu.myMC[i][j], end = " ")
				print(wu.myMC[i][-1])
		else:
			print("invalid command")
		
		#  Write to stable storage
		stable_storage.store()

		# Wait for next command
		command = input().split(" ")

	print("exiting...")
	os._exit(0)

def handle_test_file():
	''' Execute a sequence of commands with timings rather than taking user input. '''
	print("Handling test file")

if __name__== "__main__":
	main()
