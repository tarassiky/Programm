import tyt
import unittest
from tyt import calculate


class TestCalculations(unittest.TestCase):
    def test_xai(self):
        self.assertEqual(calculate(3, 4, "+"), 7)


if __name__ == '__main__':

    unittest.main()
