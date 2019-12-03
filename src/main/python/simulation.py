from src.main.python.bins import Bins
from src.main.python.dice import Dice


class Simulation:


    def __init__(self, numberdice, numberrolls):
        self.numberOfDice = numberdice
        self.numberOfRolls = numberrolls
        self.dice = Dice(self.numberOfDice)
        self.bins = Bins(self.numberOfDice)

    def runSimulation(self):
        self.bins.create_bin()
        for i in range(self.numberOfRolls):
            dicesum = self.dice.tossAndSum()
            self.bins.increment_bin(dicesum)
        self.printStars(self.bins.list)



    def printStars(self, list):
        for x in list:
            stars = ""
            for y in range(1, int(100*x/self.numberOfRolls)):
                stars = stars + "*"

            print("sum: %-5s  times: %-7s percent: %-9s : %s" % (list.index(x) + self.numberOfDice, x, x/self.numberOfRolls, stars))
