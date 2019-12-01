import unittest
from src.main.python.bins import createBin
from src.main.python.dice import tossAndSum
from src.main.python.simulation import runSimulation
from src.main.python.simulation import printStars


class TestDiceyLab(unittest.TestCase):
    def test_createBin(self):
        res = createBin(5)
        self.assertTrue(res, 150)

    def test_tossandSum(self):
        num = tossAndSum(3)
        self.assertTrue(num, int)

    #def test_runSimulation(self):
        #sim = runSimulation()
        #self.assertTrue(sim, 3)

    #def test_printStars(self):
        #stars



if __name__ == '__main__':
    unittest.main()
