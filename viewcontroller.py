import sys
import time
import json
import implementation as imp

def main():
	siteID = sys.argv[1]

	with open('knownhosts.json') as hosts_file:
		hosts = json.load(hosts_file)['hosts']

	hostToID = dict()
	count = 0
	for key in sorted(hosts.keys()):
		hostToID[key] = count
		count += 1

	if len(sys.argv) >= 3:
		handle_test_file()
	else:
		wu = imp.Wuubern(len(hosts) ,hostToID[siteID])
		handle_user_input(wu)


def read_stable_storage():
	''' If a stable storage file was written in this directory, read it to load dictionary '''
	pass

def handle_user_input(wu):
	''' Main loop for handling user input. '''
	print("Handling user input")

	command = input().split(" ")
	counter = 0
	while command[0] != 'quit':
		if command[0] == "reserve":
			counter += 1
			ev = e.Event("Reservation", counter, hostToID[siteID])
			ev.resInfo(command[1], "pending", command[2])
			wu.insert(ev)
			print("reserve command received")

		elif command[0] == "cancel":
			for e in wu.dct:
				if(e.resUser == command[1]):
					wu.delete(ev)
					break
			print("cancel command received")

		elif command[0] == "view":
			for ev in wu.dct:
				print(ev.resUser , ev.resPlaneList, ev.resStatus)
			print("view command received")

		elif command[0] == "log":
			for ev in wu.log:
				print(ev.type, ev.inserted.resUser, ev.inserted.resPlaneList)
			print("log command received")

		elif command[0] == "send":
			np, myMC = wu.send(hostToID[command[1]])
			if(len(commmand > 2)):
				#if there is a message
			#add udp stuff
			print("send command received")

		elif command[0] == "sendall":
			for id in hostToID.values():
				np, myMC = wu.send(id)
				#add udp stuff
			print("sendall command received")

		elif command[0] == "clock":
			print("clock command received")
			for i in range(len(wu.myMC)):
				for j in range(len(wu.myMC[i]) -1):
					print(wu.myMC[i][j], end = " ")
				print(wu.myMC[i][-1])
		else:
			print("invalid command")
		
		# Wait for next command
		command = input().split(" ")

	print("exiting...")

def handle_test_file():
	''' Execute a sequence of commands with timings rather than taking user input. '''
	print("Handling test file")

if __name__== "__main__":
	main()
