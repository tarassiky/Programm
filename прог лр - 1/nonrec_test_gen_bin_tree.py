import unittest
from nonrec_gen_bin_tree import not_rec_gen_bin_tree  # Импортируем нерекурсивную версию


class TestGenBinTreeNonRecursive(unittest.TestCase):

    def test_height_zero(self):
        """Тестируем нулевую высоту"""
        tree = not_rec_gen_bin_tree(h=0, root=4)
        self.assertEqual(tree, {"4": []})  # Нулевой уровень должен вернуть один узел

    def test_height_one(self):
        """Тестируем высоту равную единице"""
        tree = not_rec_gen_bin_tree(h=1, root=4)
        self.assertEqual(tree, {"4": ["12", "8"], "12": [], "8": []})  # Исправлено ожидание

    def test_height_two(self):
        """Тестируем высоту равную двум"""
        tree = not_rec_gen_bin_tree(h=2, root=3)
        expected_tree = {
            '11': [],
            '13': [],
            '21': [],
            '27': [],
            '3': ['9', '7'],
            '7': ['21', '11'],
            '9': ['27', '13']
        }
        self.assertEqual(tree, expected_tree)


if __name__ == "__main__":
    unittest.main()