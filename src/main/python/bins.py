class Bins:

    def __init__(self, numrolls):
        self.numberOfRolls = numrolls

    def create_bin(self):
        list = []
        for x in range(self.numberOfRolls, self.numberOfRolls * 6):
            list.append(0)

        return list
