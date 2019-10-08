class Event:

	def __init__(self, typ, timeStamp, pid):
		self.time = timeStamp
		#possible types are: res_pend, res_conf, insert, delete
		self.type = typ
		self.pID = pis
		self.inserted = None
		self.deleted = None

	def insertOf(event):
		if self.type is not "insert":
			print("ERROR: Trying to add an insert event for non-insert event")
		else:
			self.inserted = event

	def deleteOf(event):
		if self.type is not "delete":
			print("ERROR: Trying to add a delete event for non-delete event")
		else:
			self.deleted = event