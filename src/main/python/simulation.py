from main.python.dice import Dice


class Simulation:
    dice1 = Dice(2)
    sum = dice1.tossandsum()
    print(sum)
