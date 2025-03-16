import unittest
from gen_bin_tree import gen_bin_tree  # Импортируем рекурсивную версию функции


class TestGenBinTreeRecursive(unittest.TestCase):

    def test_height_zero(self):
        """Тестируем нулевую высоту"""
        tree = gen_bin_tree(h=0, root=4)
        self.assertEqual(tree, {"4": []})  # Дерево должно содержать один узел без детей

    def test_height_one(self):
        """Тестируем высоту равную единице"""
        tree = gen_bin_tree(h=1, root=4)
        self.assertEqual(tree, {"4": [{"12": []}, {"8": []}]})  # Исправляем ожидание

    def test_height_two(self):
        """Тестируем высоту равную двум"""
        tree = gen_bin_tree(h=2, root=3)
        expected_tree = {
            "3": [
                {"9": [{"27": []}, {"13": []}]},
                {"7": [{"21": []}, {"11": []}]}
            ]
        }
        self.assertEqual(tree, expected_tree)  # Исправляем ожидание


if __name__ == "__main__":
    unittest.main()