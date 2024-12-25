import pytest
from extwo import two_sum

@pytest.mark.parametrize(
    "lst, expected_result",
    [
        ([6, 3, 6, 1, 8, 12, 6, 5, 6], (3, 7)),  #Базовый случай: Пара (6, 6) на индексах 0 и 2
        ([2, 4, 6, 8, 10], (0, 1)),  #Базовый случай: Пара (4, 10) на индексах 1 и 4
        ([5, 1], (0, 1)),  #Пограничный случай: Минимальный размер массива, пара (7, 1) на индексах 0 и 1
        ([10 ** 9, -10 ** 9], None),  #Пограничный случай: Пара не найдена, возвращается None
        ([10 ** 9, 10 ** 9 - 2, -10 ** 9], None),  #Пограничный случай: Нет пары с суммой 8
        ([2, 2, 2, 2], None),  #Особый случай: Все числа одинаковые, нет подходящей пары
        ([9, 3, 3, 9, 5], (1, 2)),  #Особый случай: Пара (3, 3) на индексах 1 и 2
        ([4, 1, 5, 4, 3], (1, 2)),  #Особый случай: Пара (4, 4) на индексах 0 и 3
        ([2, 5, 1, 4, 3], (0, 3)),  #Особый случай: Пара (2, 4) на индексах 0 и 3
        ([], None),  #Особый случай: Пустой массив, возвращается None
    ]
)
def test_two_sum(lst, expected_result):
    """Тестирует функцию two_sum с параметризацией."""
    assert two_sum(lst) == expected_result

