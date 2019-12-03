import unittest
from src.main.python.bins import Bins
from src.main.python.dice import Dice
from src.main.python.simulation import Simulation


class TestDiceyLab(unittest.TestCase):
    def test_createBin(self):
        bins = Bins(5)
        bins.create_bin()
        self.assertTrue(len(bins.list), 26)

    def test_tossAndSum(self):
        for x in range(0, 10000):
            num = Dice(5).tossAndSum()
            self.assertTrue(num <= 30)
            self.assertTrue(num >= 5)



if __name__ == '__main__':
    unittest.main()
