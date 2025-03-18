import random
import timeit
import matplotlib.pyplot as plt


def setup_data(n: int) -> list:
    """Генерация списка случайных значений корней и высот деревьев."""
    min_root = 1      # Минимальное значение корня
    max_root = 200    # Максимальное значение корня
    min_height = 1    # Минимальная высота дерева
    max_height = 15   # Максимальная высота дерева

    data = []
    for _ in range(n):
        root = random.randint(min_root, max_root)
        height = random.randint(min_height, max_height)
        data.append((root, height))  # Добавляем пару (root, height) в список

    return data


def calculate_time(n: int, func) -> float:
    """Измеряет общее время выполнения функции func для n пар (root, height)."""
    data = setup_data(n)
    delta = 0
    for root, height in data:
        start_time = timeit.default_timer()
        func(root, height)
        delta += timeit.default_timer() - start_time
    return delta


def gen_bin_tree1(root=2, height=6, left_leaf=lambda arg: int(arg) * 3, right_leaf=lambda arg: int(arg) + 4):
    """
    Рекурсивная функция для генерации бинарного дерева.
    :param root: Корень дерева
    :param height: Высота дерева
    :param left_leaf: Функция для вычисления левого потомка
    :param right_leaf: Функция для вычисления правого потомка
    :return: Словарь, представляющий дерево
    """
    tree = {}

    def tree_build(root2, height2):
        """Рекурсивная вспомогательная функция для построения дерева."""
        if height2 > 0:
            left_leaf_value = left_leaf(root2)  # Вычисляем левый потомок
            right_leaf_value = right_leaf(root2)  # Вычисляем правый потомок

            tree[root2] = [
                {left_leaf_value: tree_build(left_leaf_value, height2 - 1)},
                {right_leaf_value: tree_build(right_leaf_value, height2 - 1)}
            ]

        else:
            return {}  # Если глубина равна нулю, возвращаем пустой словарь

        return tree[root2]

    if height == 0:
        return {root: []}

    return {root: tree_build(root, height)}


def gen_bin_tree2(root, height, left_leaf=lambda arg: int(arg) * 3, right_leaf=lambda arg: int(arg) + 4):
    """
    Нерекурсивная функция для генерации бинарного дерева.
    :param root: Корень дерева
    :param height: Высота дерева
    :param left_leaf: Функция для вычисления левого потомка
    :param right_leaf: Функция для вычисления правого потомка
    :return: Словарь, представляющий дерево
    """
    tree = {}

    if height == 0:
        return {root: []}

    stack = [(root, height)]  # Стартуем с корнем и полной высотой

    while stack:
        current, current_height = stack.pop()

        if current_height > 1:  # Если глубина больше 1, добавляем дочерние узлы
            left_leaf_value = left_leaf(current)
            right_leaf_value = right_leaf(current)
            stack.append((left_leaf_value, current_height - 1))
            stack.append((right_leaf_value, current_height - 1))

        # Создаем текущий узел с дочерними элементами или пустым списком
        tree[current] = []
        if current_height == 1:  # Если следующая глубина должна быть нулевой, добавляем пустые списки
            tree[current].extend([])  # Добавляем пустой список как дочерний элемент
        elif current_height > 1:  # Иначе добавляем реальные узлы
            tree[current].extend([{left_leaf_value}, {right_leaf_value}])  # Используем фигурные скобки для представления узлов

    return tree


def main():
    """Основная функция для измерения производительности и построения графиков."""
    # Графики времени выполнения для рекурсивной и нерекурсивной версий
    recursive_times = []
    iterative_times = []

    for n in range(10, 101, 10):  # Измеряем для n от 10 до 100 с шагом 10
        recursive_times.append(calculate_time(n, gen_bin_tree1))
        iterative_times.append(calculate_time(n, gen_bin_tree2))

    plt.figure(figsize=(12, 6))
    plt.title("Сравнение времени выполнения рекурсивной и нерекурсивной версий")
    plt.xlabel("Размер списка (n)")
    plt.ylabel("Общее время выполнения (секунды)")

    # Строим графики для рекурсивной и нерекурсивной версий
    plt.plot(range(10, 101, 10), recursive_times, label="Рекурсия")
    plt.plot(range(10, 101, 10), iterative_times, label="Нерекурсия")

    plt.legend()  # Легенда для обозначения графиков
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()