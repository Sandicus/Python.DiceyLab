import random


class Dice:

    def __init__(self, numDice):
        self.numberOfDice = numDice

    def tossAndSum(self):
        toss = 0
        for i in range(self.numberOfDice):
            toss = toss + random.randint(1, 6)
        return toss
