from dice import Dice


class Simulation:
        dice1 = Dice(2)
        bin = bins(2)

        for x in range (1, 1000000):
            sum = dice1.tossandsum()
            bin[sum] = bin[sum] + 1


        for x in bin:
            print(x + "  |")
            print(bin[x] +  "  |")
            print(bin[x / 1000000 + "  |"])
            for x in range(1,bin[x]):
                print ("*")
