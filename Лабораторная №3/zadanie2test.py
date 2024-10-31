import unittest
import statistics
from zadanie2 import calculate

class TestCalculate(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate('+', 1, 2, 3), 6)
        self.assertAlmostEqual(calculate('+', 1.1, 2.2, 3.3), 6.6)

    def test_subtraction(self):
        self.assertEqual(calculate('-', 10, 5, 3), 2)
        self.assertAlmostEqual(calculate('-', 10.5, 5.2, 3.1), 2.2)

    def test_multiplication(self):
        self.assertEqual(calculate('*', 2, 3, 4), 24)
        self.assertAlmostEqual(calculate('*', 2.5, 3.5, 4.5), 39.375)

    def test_division(self):
        self.assertEqual(calculate('/', 10, 2), 5)
        self.assertAlmostEqual(calculate('/', 10.5, 2.1), 5)
        self.assertEqual(calculate('/', 10, 0), "Деление на ноль невозможно!")
        self.assertEqual(calculate('/', 10, 2, 0), "Деление на ноль невозможно!")

    def test_medium(self):
        self.assertAlmostEqual(calculate('medium', 1, 2, 3, 4, 5), 3)
        self.assertAlmostEqual(calculate('medium', 1.5, 2.5, 3.5, 4.5, 5.5), 3.5)

    def test_variance(self):
        self.assertAlmostEqual(calculate('variance', 1, 2, 3, 4, 5), 2.5)
        self.assertAlmostEqual(calculate('variance', 1.5, 2.5, 3.5, 4.5, 5.5), 2.5)


    def test_std_deviation(self):
        self.assertAlmostEqual(calculate('std_deviation', 1, 2, 3, 4, 5), 1.581139)
        self.assertAlmostEqual(calculate('std_deviation', 1.5, 2.5, 3.5, 4.5, 5.5), 1.581139)

    def test_median(self):
        self.assertEqual(calculate('median', 1, 2, 3, 4, 5), 3)
        self.assertEqual(calculate('median', 1, 2, 3, 4, 5, 6), 3.5)


    def test_iqr(self):
        self.assertEqual(calculate('iqr', 1, 2, 3, 4, 5, 6, 7, 8), 4.5)
        self.assertEqual(calculate('iqr', 1,3,5,7,9,11,13), 8)

    def test_incorrect_operation(self):
        self.assertEqual(calculate('incorrect', 1, 2), "Некорректная операция!")

    def test_zero_division_error(self):
        self.assertEqual(calculate('/', 10, 0), "Деление на ноль невозможно!")


if __name__ == '__main__':
    unittest.main()