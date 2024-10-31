import unittest
from zadanie1 import calculate

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3, '+'), 5)
        self.assertEqual(calculate(-5, 10, '+'), 5)
        self.assertEqual(calculate(0, 0, '+'), 0)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 2, '-'), 3)
        self.assertEqual(calculate(10, -3, '-'), 13)
        self.assertEqual(calculate(0, 0, '-'), 0)

    def test_multiplication(self):
        self.assertEqual(calculate(4, 6, '*'), 24)
        self.assertEqual(calculate(-2, 5, '*'), -10)
        self.assertEqual(calculate(0, 5, '*'), 0)
        self.assertEqual(calculate(5, 0, '*'), 0)

    def test_division(self):
        self.assertEqual(calculate(10, 2, '/'), 5)
        self.assertEqual(calculate(15, 3, '/'), 5)
        self.assertEqual(calculate(0, 5, '/'), 0)  # Деление нуля на число

    def test_invalid_operation(self):
        self.assertEqual(calculate(2, 3, 'invalid'), "Некорректная операция!")

    def test_floating_point_numbers(self):
        self.assertEqual(calculate(2.5, 3.5, '+'), 6)
        self.assertEqual(calculate(7.2, 2.8, '-'), 4.4)
        self.assertEqual(calculate(2.5, 2, '*'), 5)
        self.assertAlmostEqual(calculate(10.0, 2.5, '/'), 4, places=1) #  Учтён rounding

    def test_zero_division(self):
        self.assertEqual(calculate(10, 0, '/'), "Деление на ноль невозможно!")
        self.assertEqual(calculate(0, 0, '/'), "Деление на ноль невозможно!")

if __name__ == '__main__':
    unittest.main()
