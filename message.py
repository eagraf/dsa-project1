class Message:
    
    def __init__(self, np, clock, message="Hello, world!"):
        self.message = message
        self.np = np
        self.clock = clock

    def __str__(self):
        return self.message + '\n' + self.np + '\n' + self.clock + '\n'