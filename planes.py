class Planes:

    def __init__(self):
        self.allPlanes = [[0, 0]  for i in range(20)]

    #returns true if spot, false if no stop
    def checkSpot(self, plane):
        if self.allPlanes[plane][0] != 0:
            if self.allPlanes[plane][1] != 0:
                return False      
        return True
    
    def bookSpot(self, plane, name):
        if self.allPlanes[plane][0] != 0:
            if self.allPlanes[plane][1] != 0:
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
            
