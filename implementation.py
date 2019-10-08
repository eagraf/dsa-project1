import event as e

class Wuu-bern:

	def __init__(self, numSites, mid):
		self.myMC = [[0] * numSites for i in range(numSites)]
		self.dct = set()
		self.log = set()
		self.counter = 0
		self.mID = mid

	def directKnowledge(self, oMC, oID):
		for i in range(len(self.myMC)):
			self.myMC[self.mID][i] = max(self.myMC[self.mID][i], oMC[oID][i])

	def indirectKnowledge(self, oMC):
		for i in range(len(self.myMC)):
			for j in range(len(self.myMC)):
				self.myMC[i][j] = max(self.myMC[i][j], oMC[i][j])

	def hasRec(self, event, otherSite):
		return myMC[otherSite][event.pID] >= event.time

	def insert(self, event):
		self.counter += 1
		self.myMC[self.mID][self.mID] =  c
		ins = e.Event("insert", c, self.mID)
		ins.insertOf(event)
		self.log.add(ins)
		self.dct.add(event)

	def delete(selfevent):
		self.counter += 1
		self.myMC[self.mID][self.mID] =  c
		de = e.Event("delete", c, mID)
		de.deleteOf(event)
		self.log.add(de)
		self.dct.remove(event)

	def send(self, oID):
		np = set()
		for ev in self.log:
			if not hasRec(self.myMC, ev, oID):
				np.add(ev)
		return np

	def recieve(self, oMC,oID, np):
		ne = set()
		for ev in np:
			if not hasRec(self.myMC, ev, self.mID):
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

		directKnowledge(oMC, oID)
		indirectKnowledge(oMC, oID)

		newLog = set()
		for ev in self.log.union(ne):
			thereExists = False
			for s in range(len(oMC)):
				if not hasRec(self.myMC, ev, s):
					thereExists = True
					break
			if thereExists:
				newLog.add(ev)

		self.log= newLog








