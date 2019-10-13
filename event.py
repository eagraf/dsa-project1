class Event:

	def __init__(self, typ, timeStamp, pid):
		self.time = timeStamp
		#possible types are: res_pend, res_conf, insert, delete, send, recieve,
		self.type = typ
		self.pID = pid
		self.inserted = None
		self.deleted = None

	def __str__(self):
		s = "Timestamp:" + str(self.time) + '\n'
		s += "Type:" + self.type + '\n'
		if(self.inserted):
			s += "Inserted Event\n"
		elif(self.deleted):
			s += "Deleted Event\n"

		return s

	def insertOf(self,event):
		if self.type is not "insert":
			print("ERROR: Trying to add an insert event for non-insert event")
		else:
			self.inserted = event

	def deleteOf(self,event):
		if self.type is not "delete":
			print("ERROR: Trying to add a delete event for non-delete event")
		else:
			self.deleted = event