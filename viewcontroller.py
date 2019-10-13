import sys
import time
import json
import implementation as imp

def main():
	siteID = sys.argv[1]

	with open('knownhosts.json') as hosts_file:
		hosts = json.load(hosts_file)['hosts']

	if len(sys.argv) >= 3:
		handle_test_file()
	else:
		handle_user_input()


def read_stable_storage():
	''' If a stable storage file was written in this directory, read it to load dictionary '''
	pass

def handle_user_input():
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

def handle_test_file():
	''' Execute a sequence of commands with timings rather than taking user input. '''
	print("Handling test file")

if __name__== "__main__":
	main()
