import random


class Dice:
    MAX = 6

    def __init__(self, numrolls):
        self.numberOfRolls = numrolls

    def tossandsum(self):
        toss = 0
        for i in range(self.numberOfRolls):
            diceroll = random.randint(1, 6)
            toss = toss + diceroll
        return toss
