# Лабораторная №1 задание 3.1


def calculate(a, b, x):
    """

    :param a: первое число
    :param b: второе число
    :param x: дествие, которое будет выполняться с числами
    :return: выводит результат математического действия

    """

    if x == 'сложение':
        return a + b
    elif x == 'вычитание':
        return a - b
    elif x == 'умножение':
        return a * b
    elif x == 'деление':
        if b == 0:
            raise ValueError("Деление на ноль!")
        return a / b


def main():

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        x = input(
            "Введите операцию (сложение, вычитание, умножение, деление): ")

        result = calculate(a, b, x)
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")


def test_x():

    assert calculate(5, 3, 'сложение') == 8
    assert calculate(5, 3, 'вычитание') == 2
    assert calculate(5, 3, 'умножение') == 15
    assert calculate(6, 3, 'деление') == 2
    try:
        calculate(5, 0, 'деление')
    except ValueError:
        assert True
    else:
        assert False


if __name__ == "__main__":
    test_x()  # Запускаем тесты перед основным кодом
    main()  # Запускаем основную функцию

