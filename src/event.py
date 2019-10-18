class Event:

	def __init__(self, typ, time, pid):
		self.timeStamp = (time,pid)
		#possible types are: reservation, insert, delete
		self.type = typ
		self.pID = pid

		self.inserted = None
		self.deleted = None

		self.resUser = None
		self.resStatus = None
		self.resPlaneList = None

	def __str__(self):
		s = "Timestamp:" + str(self.timeStamp[0]) +',' +str(self.timeStamp[1]) + '\t'
		s += "Type:" + self.type + '\t'
		if(self.inserted):
			s += "Inserted Event\t"
		elif(self.deleted):
			s += "Deleted Event\t"

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

	def resInfo(self,user, rstat, planes):
		if self.type is not "Reservation":
			print("ERROR: Trying to add Reservation info for non-reservation event")
		else:
			self.resUser = user
			self.resStatus = rstat
			self.resPlaneList = planes

	def __eq__(self, other):
		return(
			self.timeStamp == other.timeStamp and
			self.type == other.type and
			self.pID == other.pID and
			self.resUser == other.resUser and
			self.resPlaneList == other.resPlaneList
			)

	def __ne__(self, other):
		return (not self == other)

	def __hash__(self):
		return hash((self.timeStamp, self.type, self.pID, self.resUser,self.resPlaneList))