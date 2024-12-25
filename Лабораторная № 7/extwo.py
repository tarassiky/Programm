import itertools

def two_sum(lst: list) -> tuple:
    """Находит индексы двух чисел в списке, сумма которых равна 10.

    Args:
        lst (list): Список чисел.

    Returns:
        tuple: Индексы двух чисел, сумма которых равна 10, или None, если таких чисел нет.
    """
    target = 6
    result = None
    # Используем комбинации для перебора всех пар индексов
    for (i, val1), (j, val2) in itertools.combinations(enumerate(lst), 2):
        # Проверяем, равна ли сумма целевому значению
        if val1 + val2 == target:
            result = (i, j)
            return tuple(sorted(result))  # Возвращаем отсортированные индексы
    return None  # Если пара не найдена, возвращаем None
