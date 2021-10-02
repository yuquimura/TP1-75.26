class GLC:

    def __init__(self, m, a, u, c):
        self.modNumber = m
        self.scalarNumber = a
        self.first = u
        self.constant = c
        self.actual = self.first

    def calculate_random(self):
        new_actual = (self.actual * self.scalarNumber + self.constant) / self.modNumber
        self.actual = new_actual
        return new_actual

    def calculate_random_uniform(self):
        return (self.calculate_random()) / self.modNumber
