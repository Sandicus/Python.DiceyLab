class Bins:

    def __init__(self, numDice):
        self.numberOfDice = numDice
        self.list = []


    def create_bin(self):
        for x in range(self.numberOfDice, self.numberOfDice * 6 + 1):
            self.list.append(0)

    def increment_bin(self,sum):
        index = sum - self.numberOfDice
        checkthis = self.list[index] + 1
        self.list[index] = checkthis