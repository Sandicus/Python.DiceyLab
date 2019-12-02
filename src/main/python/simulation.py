from src.main.python.bins import Bins
from src.main.python.dice import Dice


# from src.main.python.bins import ?????


class Simulation:
    dice1 = Dice(2)
    bin = Bins(2)

def __init__(self, numberdice, numberrolls):
    self.numberOfDice = numberdice
    self.numberOfRolls = numberrolls


def runSimulation(self):
    for i in range(self.numberOfRolls):
        dice1 = Dice(self.numberOfDice)
        dicesum = dice1.tossandsum()
        bin[dicesum] = bin[dicesum] + 1


def printStars(bin):
    for x in bin:
        print(x + "  |")
        print(bin[x] + "  |")
        print(bin[x / 1000000 + "  |"])
        for y in range(1, bin[x]):
            print("*")
