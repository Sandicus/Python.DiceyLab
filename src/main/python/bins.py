

class Bins:

    def __init__(self, numrolls):
        self.numberOfRolls = numrolls

    def createBin(self):
        bin = {}
        for x in range (self.numberOfRolls, self.numberOfRolls * 6):
            result ={x:0}
            bin.append(result)


        return bin

