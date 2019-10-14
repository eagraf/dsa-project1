import sys
import os
import time
import json
import implementation as imp
from messenger import Messenger

def main():
	siteID = sys.argv[1]

	with open('knownhosts.json') as hosts_file:
		hosts = json.load(hosts_file)['hosts']

	messenger = Messenger(hosts[siteID])

	if len(sys.argv) >= 3:
		handle_test_file()
	else:
		handle_user_input(messenger, hosts)


def read_stable_storage():
	''' If a stable storage file was written in this directory, read it to load dictionary '''
	pass

def handle_user_input(messenger, hosts):
	''' Main loop for handling user input. '''
	print("Handling user input")

	command = input().split(" ")
	while command[0] != 'quit':
		if command[0] == "reserve":
			print("reserve command received")
		elif command[0] == "cancel":
			print("cancel command received")
		elif command[0] == "view":
			print("view command received")
		elif command[0] == "log":
			print("log command received")
		elif command[0] == "send":
			print("send command received")
			host = command[1]
			messenger.send((hosts[host]['ip_address'], hosts[host]['udp_end_port']))
		elif command[0] == "sendall":
			print("sendall command received")
		elif command[0] == "clock":
			print("clock command received")
			'''for i in range(len(wuuuu.myMC)):
				for j in range(len(wuuuu.myMC[i]) -1):
					print(wuuuu.myMC[i][j], end = " ")
				print(wuuuu.myMC[i][-1])'''
		else:
			print("invalid command")
		
		# Wait for next command
		command = input().split(" ")

	print("exiting...")
	os._exit(0)

def handle_test_file():
	''' Execute a sequence of commands with timings rather than taking user input. '''
	print("Handling test file")

if __name__== "__main__":
	main()
