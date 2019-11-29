import random


class Dice:
    MAX = 6

    def __init__(self, numrolls):
        self.numberOfRolls = numrolls

    def tossandsum(self):
        toss = 0
        for i in range(self.numberOfRolls):
            toss = toss + random.randint(1, 6)
        return toss
