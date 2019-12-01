import unittest
from src.main.python.bins import createBin


class TestDiceyLab(unittest.TestCase):
    def test_createBin(self):
        res = createBin(5)
        self.assertTrue(res, 150)



if __name__ == '__main__':
    unittest.main()
