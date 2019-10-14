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
		print(self.dct)
		print("The current log looks like:")
		print(self.log)
		print("Counter:" , self.counter)
		print("My process id is:" , self.mID)
		print()

		return

	def directKnowledge(self, oMC, oID):
		for i in range(len(self.myMC)):
			self.myMC[self.mID][i] = max(self.myMC[self.mID][i], oMC[oID][i])

	def indirectKnowledge(self, oMC):
		for i in range(len(self.myMC)):
			for j in range(len(self.myMC)):
				self.myMC[i][j] = max(self.myMC[i][j], oMC[i][j])

	def hasRec(self, event, otherSite):
		return self.myMC[otherSite][event.pID] >= event.time

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
		de = e.Event("delete", self.counter, mID)
		de.deleteOf(event)
		self.log.add(de)
		self.dct.remove(event)

	def send(self, oID):
		np = set()
		for ev in self.log:
			if not self.hasRec(ev, oID):
				np.add(ev)
		return np, self.myMC

	def receive(self, oMC,oID, np):
		ne = set()
		for ev in np:
			if not self.hasRec(ev, self.mID):
				ne.add(ev)

		insertEvents = set()
		deleteEvents = set()
		for ev in ne:
			if ev.type == "insert":
				if ev.inserted == None:
					print("ERROR: no insert event????")
				else:
					insertEvents.add(ev.inserted)
			if ev.type == "delete":
				if ev.deleted == None:
					print("ERROR: no delete event????")
				else:
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








