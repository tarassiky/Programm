import json
from exceptions_for_gen_bin_tree import *

def gen_bin_tree(h=6, root=2, left_leaf=lambda arg: int(arg) * 3, right_leaf=lambda arg: int(arg) + 4):
    # Проверка корректности высоты
    if not isinstance(h, int):
        raise InvalidHeightException(h)
    if h < 0:
        raise InvalidHeightException(h)

    # Инициализация дерева
    tree = {str(root): []}

    # Базовый случай: высота равна нулю
    if h == 0:
        return tree
    else:
        # Рекурсивный вызов для левого и правого потомков
        tree[str(root)].append(gen_bin_tree(h=h - 1, root=left_leaf(root), left_leaf=left_leaf, right_leaf=right_leaf))
        tree[str(root)].append(gen_bin_tree(h=h - 1, root=right_leaf(root), left_leaf=left_leaf, right_leaf=right_leaf))

        return tree

# Пример использования
if __name__ == "__main__":
    # Генерация и вывод дерева
    result = gen_bin_tree()
    print(json.dumps(result, indent=4, ensure_ascii=False))