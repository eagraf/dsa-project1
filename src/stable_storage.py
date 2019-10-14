import pickle
from implementation import Wuubern

# TODO make this a wrapper for Wuubern
class StableStorage:

    def __init__(self):
        self.process = None

    def store(self):
        ''' Pickle the process state and store in a file. '''
        pickle.dump(self.process, open(str(self.process.mID) + '.p','wb'))

    def receive(self, clock, pID, np):
        ''' Listener function called whenever messenger receives a new message. '''
        self.store()

    def initialize(self, numSites, siteID):
        try:
            self.process = pickle.load(open(str(siteID) + '.p', 'rb'))
        except FileNotFoundError:
            self.process = Wuubern(numSites, siteID)

        return self.process