from collections import Counter

import matplotlib.pyplot as plt


class GLC:

    def __init__(self, m, a, u, c):
        self.modNumber = m
        self.scalarNumber = a
        self.first = u
        self.constant = c
        self.actual = self.first

    def calculate_random(self):
        new_actual = (self.actual * self.scalarNumber + self.constant) % self.modNumber
        self.actual = new_actual
        return new_actual

    def calculate_random_uniform(self):
        return (self.calculate_random()) / self.modNumber

    def calculate_multiple_random_uniform(self, iterations):
        values = []
        for i in range(iterations):
            value = self.calculate_random_uniform()
            values.append(value)
            print(value)
        return values

    def create_plot(self):
        random_values = self.calculate_multiple_random_uniform(1001)
        random_values = Counter(random_values)
        fig, ax = plt.subplots()
        n, bins, patches = ax.hist(random_values, 100, density=False)
        fig.tight_layout()
        plt.show()
        print(random_values)
