from collections import deque
import json
from exceptions_for_gen_bin_tree import *

def not_rec_gen_bin_tree(h=6, root=2, left_leaf=lambda arg: int(arg) * 3, right_leaf=lambda arg: int(arg) + 4):

    # Проверяем высоту на валидность
    if not isinstance(h, int):
        raise InvalidHeightException(h)
    if h < 0:
        raise InvalidHeightException(h)

    # Инициализируем дерево и очередь
    tree = {}
    queue = deque([(root, h)])  # Используем очередь для обхода уровней

    # Обрабатываем узлы до тех пор, пока очередь не пуста
    while queue:
        node_value, level = queue.popleft()  # Извлекаем пару (значение, уровень)

        if level > 0:
            # Создаем потомков и добавляем их в очередь
            left_child = left_leaf(node_value)
            right_child = right_leaf(node_value)
            tree[str(node_value)] = [str(left_child), str(right_child)]
            queue.extend([
                (left_child, level - 1),
                (right_child, level - 1)
            ])
        else:
            # Листья имеют пустое значение
            tree[str(node_value)] = []

    return tree


if __name__ == '__main__':
    # Генерируем и выводим дерево
    result = not_rec_gen_bin_tree()
    print(json.dumps(result, indent=4, ensure_ascii=False))