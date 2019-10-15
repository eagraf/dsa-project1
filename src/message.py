class Message:
    
    def __init__(self, np, clock, siteID, message="Hello, world!"):
        self.message = message
        self.np = np
        self.clock = clock
        self.siteID = siteID

    def __str__(self):
        return self.message + '\n' + self.np.__str__() + '\n' + self.clock.__str__() + '\n'