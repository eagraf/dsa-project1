class Planes:

    def __init__(self):
        self.allPlanes = [[0, 0]  for i in range(20)]

    #returns true if spot, false if no stop
    def checkSpot(self, plane):
        if self.allPlanes[plane][0] != 0 and self.allPlanes[plane][0] != name:
            if self.allPlanes[plane][1] != 0 and self.allPlanes[plane][1] != name:
                return False      
        return True

    def checkPlanes(planesList):    
        spotsLeft = True
		plns = planesList.split(',')
		plns = [int(x) for x in plns]
		for pln in plns:
			if(not self.checkSpot(pln)):
				spotsLeft = False
				break
        return spotsLeft
    
    def bookSpot(self, plane, name):
        if self.allPlanes[plane][0] != 0 and self.allPlanes[plane][0] != name:
            if self.allPlanes[plane][1] != 0 and self.allPlanes[plane][1] != name:
                print("ERROR in booking spot")
                return False 
            self.allPlanes[plane][1] = name
        else:
            self.allPlanes[plane][0] = name
        return True

    def removeSpot(self, plane, name):
        if self.allPlanes[plane][0] != name:
            if self.allPlanes[plane][1] != name:
                print("ERROR", name, "is not on this plane")
                return False
            self.allPlanes[plane][1] = 0
        else:
            self.allPlanes[plane][0] = 0
        return True

    def reservationPending(self, name, myID, numProcesses):
        users[name] = list()
        for i in range(numProcesses):
            if (i != myID):
                users[name].append(i)
    
    def recieve(self, plane, currRecieve, wudict):
        for user in users.keys():
            users[user].remove(currRecieve)
        
        for user in users.keys():
            if len(users[user]) == 0:
                self.changeStatus(user, wudict)

    def changeStatus(self, user, wudict):
        for ev in sorted(wu.dct, key=lambda event: event.timeStamp):
            spotsLeft = checkPlanes(ev.resPlaneList)
            if spotsLeft:
                plns = ev.resPlaneList.split(',')
		        plns = [int(x) for x in plns]
                for pln in plns:
                    self.bookSpot(pln, ev.resUser)
                ev.resStatus = "confirmed"
            else:
                counter += 1
                wu.delete(ev)
            if(ev.resUser == user):
                break
            



            
