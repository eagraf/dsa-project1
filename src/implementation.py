import event as e

class Wuubern:

	def __init__(self, numSites, mid):
		self.myMC = [[0] * numSites for i in range(numSites)]
		self.dct = set()
		self.log = set()
		self.counter = 0
		self.mID = mid

	def printAll(self):
		s = "The current matrix clock is:\n"
		for i in range(len(self.myMC)):
			s = s + "["
			for j in range(len(self.myMC[i])):
				s= s + str(self.myMC[i][j]) +'\t'
			s = s + "]\n"
		print(s[:-1])

		print("The current dictionary looks like:")
		for ev in self.dct:
			print(ev)
		print("The current log looks like:")
		for ev in self.log:
			print(ev)
		print("Counter:" , self.counter)
		print("My process id is:" , self.mID)
		print()

		return

	# Helper functions
	def directKnowledge(self, oMC, oID):
		for i in range(len(self.myMC)):
			self.myMC[self.mID][i] = max(self.myMC[self.mID][i], oMC[oID][i])

	def indirectKnowledge(self, oMC):
		for i in range(len(self.myMC)):
			for j in range(len(self.myMC)):
				self.myMC[i][j] = max(self.myMC[i][j], oMC[i][j])

	def hasRec(self, event, otherSite):
		return self.myMC[otherSite][event.pID] >= event.timeStamp[0]

	def happensBefore(self, mc1, mc2):
		for i in range(len(mc1)):
			for j in range(mc1[i]):
				if mc2[i][j] > mc1[i][j]:
					return False
		return True

	def concurrent(self, mc1, mc2):
		return (not self.happensBefore(mc1, mc2) and not self.happensBefore(mc2, mc1))

	def insert(self, event):
		self.counter += 1
		self.myMC[self.mID][self.mID] =  self.counter
		ins = e.Event("insert", self.counter, self.mID)
		ins.insertOf(event)
		self.log.add(ins)
		self.dct.add(event)

	def delete(self, event):
		self.counter += 1
		self.myMC[self.mID][self.mID] =  self.counter
		de = e.Event("delete", self.counter, self.mID)
		de.deleteOf(event)
		self.log.add(de)
		self.dct.remove(event)

	def send(self, oID):
		np = set()
		for ev in self.log:
			if not self.hasRec(ev, oID):
				np.add(ev)
		return np, self.myMC

	def receive(self, oMC, oID, np):
		ne = set()
		#print(np)
		'''
		for ev in np:
			if self.hasRec(ev, self.mID):
				print("HEREEEE")
				if ev.type == "insert":
					print(ev.inserted.resStatus)
					self.dct.remove(ev.inserted)
					self.dct.add(ev.inserted)
				if ev.type == "delete":
					self.dct.remove(ev.deleted)
					self.dct.add(ev.deleted)
				self.log.remove(ev)
				self.log.add(ev)
		'''
		for ev in np:
			if not self.hasRec(ev, self.mID):
				ne.add(ev)
		#print(ne)

		insertEvents = set()
		deleteEvents = set()
		for ev in ne:
			#thereExists = False
			if ev.type == "insert":
				#if ev.inserted == None:
				#	print("ERROR: no insert event????")
				#else:
				insertEvents.add(ev.inserted)
			if ev.type == "delete":
				#if ev.deleted == None:
				#	print("ERROR: no delete event????")
				#else:
					#print("AT DELETE")
					deleteEvents.add(ev.deleted)


		v = set()
		for ev in self.dct:
			if ev not in deleteEvents:
				v.add(ev)
		for ev in insertEvents:
			if ev not in deleteEvents:
				v.add(ev)
		self.dct = v

		self.directKnowledge(oMC, oID)
		self.indirectKnowledge(oMC)

		newLog = set()
		for ev in self.log.union(ne):
			thereExists = False
			for s in range(len(oMC)):
				if not self.hasRec(ev, s):
					thereExists = True
					break
			if thereExists:
				newLog.add(ev)

		self.log= newLog
	
	def getUsers(self, np):
		users = set()
		userPlanes = dict()
		for ev in np:
			if ev.type == "insert":
				plns = list()
				if ev.inserted.resPlaneList != None:
					plns = ev.inserted.resPlaneList.split(',')
					plns = [int(x) for x in plns]
				users.add(ev.inserted.resUser)
				userPlanes[ev.inserted.resUser] = plns
		return users, self.mID, userPlanes

	







