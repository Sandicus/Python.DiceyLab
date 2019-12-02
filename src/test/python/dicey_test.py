import unittest
from src.main.python.bins import Bins
from src.main.python.dice import Dice
from src.main.python.simulation import runSimulation
from src.main.python.simulation import printStars


class TestDiceyLab(unittest.TestCase):
    def test_createBin(self):
        res = Bins(5).createBin()
        self.assertTrue(res, 150)

    def test_tossAndSum(self):
        num = Dice().tossAndSum(3)
        self.assertTrue(num, int)

    #def test_runSimulation(self):
        #sim = runSimulation()
        #self.assertTrue(sim, 3)

    #def test_printStars(self):
        #stars



if __name__ == '__main__':
    unittest.main()
