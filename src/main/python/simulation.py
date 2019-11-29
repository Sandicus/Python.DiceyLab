from src.main.python.dice import Dice


class Simulation:

    def __init__(self, numberdice, numberrolls):
        self.numberOfDice = numberdice
        self.numberOfRolls = numberrolls

    def runSimulation(self):
        for i in range(self.numberOfRolls):
            dice1 = Dice(self.numberOfDice)
            dicesum = dice1.tossandsum()
            print(dicesum)
            # add dicesum to bin
