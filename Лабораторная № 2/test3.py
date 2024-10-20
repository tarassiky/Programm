import unittest
import task3

from task3 import decay_amount

class TestCalculations(unittest.TestCase):

    def test_Sr_90(self):
        self.assertEqual(task3.radioactive_funcs["Sr_90"](100, 4006.9 * 365 * 24 * 3600), 1.3126731745626446e-40)

    def test_C_14(self):
        self.assertEqual(task3.radioactive_funcs["C_14"](100, 4006.9 * 365 * 24 * 3600), 61.58775872426274)

    def test_Co_60(self):
        self.assertEqual(task3.radioactive_funcs["Co_60"](100, 4006.9 * 365 * 24 * 3600), 1.3185507349706862e-227)


if __name__ == '__main__':

    unittest.main()