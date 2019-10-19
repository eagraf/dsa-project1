class Planes:

    def __init__(self):
        self.allPlanes = [[0, 0]  for i in range(20)]
        self.users = dict()

    #returns true if spot, false if no stop
    def checkSpot(self, plane, name):
        if self.allPlanes[plane][0] != 0 and self.allPlanes[plane][0] != name:
            if self.allPlanes[plane][1] != 0 and self.allPlanes[plane][1] != name:
                return False      
        return True

    def checkPlanes(self, planesList, name):    
        spotsLeft = True
        plns = planesList.split(',')
        plns = [int(x) for x in plns]
        for pln in plns:
            if(not self.checkSpot(pln, name)):
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

    def addUser(self, name, myID, numProcesses):
        self.users[name] = list()
        for i in range(numProcesses):
            if (i != myID):
                self.users[name].append(i)
        #print(self.users)

    def receiveAdd(self, names, myID, numProcesses):
        for name in names:
            if name not in self.users.keys():
                self.users[name] = list()
                for i in range(numProcesses):
                    if (i != myID):
                        self.users[name].append(i)
        #print(self.users)
    
    def receive(self,currRecieve, wu):
        print(self.users)
        for user in self.users.keys():
            print(currRecieve)
            if currRecieve in self.users[user]:
                self.users[user].remove(currRecieve)
        
        for user in self.users.keys():
            if len(self.users[user]) == 0:
                self.changeStatus(user, wu)
        print(self.allPlanes)

    def changeStatus(self, user, wu):
        for ev in sorted(wu.dct, key=lambda event: event.timeStamp):
            spotsLeft = self.checkPlanes(ev.resPlaneList, ev.resUser)
            if spotsLeft:
                plns = ev.resPlaneList.split(',')
                plns = [int(x) for x in plns]
                for pln in plns:
                    self.bookSpot(pln, ev.resUser)
                ev.resStatus = "confirmed"
            else:
                #counter += 1
                wu.delete(ev)
            if(ev.resUser == user):
                break
            



            
