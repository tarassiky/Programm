import tr
import unittest
from tr import calculate


class TestCalculations(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(calculate(8, 2, "+"), 10.0)
        self.assertEqual(calculate(12, 6, "/"), 2.0)
        self.assertEqual(calculate(15, 4, "-"), 11.0)
        self.assertEqual(calculate(6, 4, "*"), 24.0)
        self.assertEqual(calculate(4, 0, "/"), "Деление на ноль невозможно!")  # Исправлено сообщение


if __name__ == '__main__':
    unittest.main()
