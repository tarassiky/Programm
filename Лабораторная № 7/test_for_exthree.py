from hypothesis import given, strategies as st
import pytest
from exthree import compute_factorial

@given(st.integers(min_value=0, max_value=100))
def test_factorial_accuracy(n):
    """Проверяет корректность вычисления факториала для допустимых значений n."""
    if n in (0, 1):
        assert compute_factorial(n) == 1
    else:
        result = compute_factorial(n)
        expected = 1
        for i in range(1, n + 1):
            expected *= i
        assert result == expected

@given(st.integers(min_value=0, max_value=99))
def test_factorial_identity(n):
    """Проверяет свойство факториала: (n + 1)! = (n + 1) * n!."""
    assert compute_factorial(n + 1) == (n + 1) * compute_factorial(n)

@given(st.integers(min_value=0, max_value=100))
def test_factorial_non_negative_value(n):
    """Убеждается, что факториал всегда возвращает неотрицательное значение."""
    assert compute_factorial(n) >= 0

@given(st.one_of(st.floats(allow_nan=False, allow_infinity=False), st.integers(max_value=-1)))
def test_factorial_invalid_arguments(n):
    """Проверяет, что функция выбрасывает ValueError для некорректных входных данных."""
    with pytest.raises(ValueError):
        compute_factorial(n)
