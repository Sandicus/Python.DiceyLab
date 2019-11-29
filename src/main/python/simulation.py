from dice import Dice


class Simulation:

    def __init__(self, numDice, numrolls):
        self.numberOfDice = numDice
        self.numberOfRolls = numrolls


    def runSimulation(self):
        for i in range(self.numberOfRolls):
            dice1 = Dice(self.numberOfDice)
            # add dice1 to bin

        sum = dice1.tossandsum()
        print(sum)