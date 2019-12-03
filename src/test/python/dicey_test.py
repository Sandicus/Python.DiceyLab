import unittest
from src.main.python.bins import Bins
from src.main.python.dice import Dice
from src.main.python.simulation import Simulation


class TestDiceyLab(unittest.TestCase):
    def test_createBin(self):
        res = Bins(5).create_bin()
        self.assertTrue(res, 150)

    def test_tossAndSum(self):
        num = Dice(5).tossAndSum()
        self.assertTrue(num, int)

    # def test_runSimulation(self):
    #     sim = Simulation(100, 100).runSimulation()
    #     self.assertTrue(sim, 3)

    #def test_printStars(self):
        #stars



if __name__ == '__main__':
    unittest.main()
