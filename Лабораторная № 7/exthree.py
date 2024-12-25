def compute_factorial(n):
    """Вычисляет факториал числа n.

    Args:
        n (int): Натуральное число.

    Returns:
        int: Факториал числа n.

    Raises:
        ValueError: Если n не является натуральным числом.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть натуральным числом")
    if n in (0, 1):
        return 1
    return n * compute_factorial(n - 1)
