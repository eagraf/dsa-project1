import pickle
from implementation import Wuubern
from planes import Planes

# TODO make this a wrapper for Wuubern
class StableStorage:

    def __init__(self):
        self.wuuBern = None
        self.planes = None
        

    def store(self):
        ''' Pickle the process state and store in a file. '''
        pickle.dump(self.wuuBern, open('wuuBern' + str(self.wuuBern.mID) + '.p','wb'))
        pickle.dump(self.planes, open('planes' + str(self.wuuBern.mID) + '.p','wb'))

    def receive(self, clock, pID, np):
        ''' Listener function called whenever messenger receives a new message. '''
        self.store()

    def initialize(self, numSites, siteID):
        try:
            self.wuuBern = pickle.load(open('wuuBern' + str(siteID) + '.p', 'rb'))
            self.planes = pickle.load(open('planes' + str(siteID) + '.p', 'rb'))
        except FileNotFoundError:
            self.wuuBern= Wuubern(numSites, siteID)
            self.planes = Planes()

        return self.wuuBern, self.planes