class GLC:

    def __init__(self, m, a, u, c):
        self.modNumber = m
        self.scalarNumber = a
        self.first = u
        self.constant = c
        self.actual = self.first

    def calculate_random(self):
        return (self.actual * self.scalarNumber + self.constant)/self.modNumber