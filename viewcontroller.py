import sys
import time
import implementation as imp

def main():
	siteID = sys.argv[1]
	knownHosts = sys.argv[2]
	inputfile = sys.argv[3]

	inputs = f.readlines()
	inputs = [x.strip() for x in inputs]

	reservationList = list()

	wuuuu= imp.WuuBern()

	for input in inputs:
		if input.isdigit():
			time.sleep(int(input))
			continue
		words = input.split()
		elif words[0] == "reserve":
			#reservation behavior
			if True:
				print("Reservation submitted for " + words[1] + ".")
			else:
				print("Cannot schedule reservation for " + words[1] + ".")

		elif words[0] == "cancel":
			#cancel behavior
			print("Reserevation for " + words[1] + " cancelled.")

		elif words[0] == "view":
			#sort reservationList
			for res in reservationList:
				print(res)

		elif words[0] == "log":
			#print wuuuu.log IN SORTED ORDER

		elif words[0] == "send":

		elif words[0] == "sendall":

		elif words[0] == "clock":
			for i in range(len(wuuuu.myMC)):
				for j in range(len(wuuuu.myMC[i]) -1):
					print(wuuuu.myMC[i][j], end = " ")
				print(wuuuu.myMC[i][-1])
				


