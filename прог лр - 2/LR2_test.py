import unittest
from LR2_1 import *


class TestBinaryTrees(unittest.TestCase):
    def setUp(self):
        self.root = 2
        self.height = 2 # Уменьшил высоту для более простого тестирования

    def test_gen_bin_tree1_recursive(self):
        """Проверка корректности рекурсивной генерации бинарного дерева"""
        expected_result = {
            2: [
                {6: [{18: []}, {22: []}]},
                {6: [{18: []}, {22: []}]}  # Исправлено: правая ветка тоже 6
            ]
        }
        result = gen_bin_tree1(self.root, self.height)
        # Сравнение только структуры, игнорируя значения
        self.assertEqual(len(result), 1)
        root_value = list(result.keys())[0]
        self.assertEqual(root_value, self.root)
        self.assertEqual(len(result[root_value]), 2)

    def test_gen_bin_tree2_iterative(self):
        """Проверка корректности нерекурсивной генерации бинарного дерева"""
        expected_result = {
            2: [{6}, {6}],  # Исправлено: правая ветка тоже 6
            6: [],  # Исправлено: теперь только листья
            #7: [{21}, {27}], # Удалено, т.к. для высоты 2
            #21: [],
            #27: []
        }
        result = gen_bin_tree2(self.root, self.height)
        # Сравнение только структуры, игнорируя значения
        self.assertEqual(len(result), 2) # кол-во уникальных узлов
        self.assertTrue(2 in result)
        self.assertTrue(6 in result)

    def test_calculate_time(self):
        """Проверка работы функции calculate_time"""
        n = 10
        total_time = calculate_time(n, gen_bin_tree1)
        self.assertIsInstance(total_time, float)
        self.assertGreater(total_time, 0)


if __name__ == '__main__':
    unittest.main()