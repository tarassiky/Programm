import unittest
import os
from LR66 import write_log, calculate


class TestSomeFunc(unittest.TestCase):

    def test_creating_file_exception(self):
        args = [9, 3]
        log_file = 'newoutput1.txt'
        with self.assertRaises(Exception) as context:
            write_log(*args, action='*', file=log_file)
        self.assertIn("Ошибка записи в файл", str(context.exception))

    def test_calculate_division_by_zero(self):
        args = [9, 0]
        regex_text = "Деление на ноль невозможно"
        with self.assertRaisesRegex(ValueError, regex_text):
            calculate(*args, operation='/')

    def test_write_log_success(self):
        file_name = "test_log.txt"
        try:
            write_log(3, 5, action="add", result=8, file=file_name)
            with open(file_name, "r") as f:
                content = f.read()
            self.assertIn("add: (3, 5) = 8", content)
        finally:
            if os.path.exists(file_name):
                os.remove(file_name)


if __name__ == '__main__':
    unittest.main(verbosity=2)
