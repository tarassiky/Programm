# Лабораторная №1 задание 3.2


def guess_number(x, low, high):
    """
    Угадывает число x методом бинарного поиска от значения low до high.

    Parameters:
        x (int): Загаданное число.
        low (int): Нижняя граница интервала для угадывания.
        high (int): Верхняя граница интервала для угадывания.

    Returns:
        int: Правильно угаданное число.
        int: Количество попыток угадывания.
    """
    attempts = 0

    while low <= high:
        attempts += 1
        guess = (low + high) // 2

        if guess == x:
            return guess, attempts
        elif guess < x:
            low = guess + 1
        else:
            high = guess - 1

    return None, attempts  # Если число не найдено


# Запрашиваем у пользователя загаданное число
x = int(input('Загадайте число в диапозоне от 0 до 100: '))
low = 0
high = 100

result, attempts = guess_number(x, low, high)

if result is not None:
    print(f"Правильное число: {result}")
    print(f"Количество попыток: {attempts}")
else:
    print("Невозможно угадать число.")

