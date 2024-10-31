import logging
import math

# Настройка логирования
logger = logging.getLogger("Calculator")
logging.basicConfig(level=logging.INFO)


def log_decorator(function):
    """Декоратор, который логирует вызовы функций.
    :param function: Функция, которую необходимо обернуть логированием.
    :return: Обернутая функция с логированием.
    """

    def wrapper(x, y, operation):
        logger.info(f'Введенные операнды и операция: {x}, {y}, {operation}')
        result = function(x, y, operation)
        logger.info("Результат: %s.", result)
        return result

    return wrapper


def convert_precision(tolerance):
    """
    Извлекает порядок значения tolerance.
    :param tolerance: Число с плавающей точкой, представляющее точность.
    :return: Порядок значения tolerance (целое число). Возвращает 0 если tolerance = 0
    :raises ValueError: Если tolerance не является числом или меньше 0.
    """
    if not isinstance(tolerance, (int, float)):
        raise ValueError("Tolerance must be a number.")
    if tolerance <= 0:
        return 0
    return int(math.floor(math.log10(tolerance))) * -1


@log_decorator
def calculate(x, y, operation):
    """
    Вычисление результата операции.
    :param x: Первое число.
    :param y: Второе число.
    :param operation: Операция для выполнения ('+', '-', '*', '/').
    :return: Округлённый результат вычисления или сообщение об ошибке.
    """
    try:
        # Устанавливаем значение по умолчанию для tolerance
        tolerance = 1e-6
        precision = convert_precision(tolerance)
    except ValueError as e:
        raise ValueError(f"Ошибка в параметре tolerance: {e}")

    if operation == '+':
        result = round(x + y, precision)
    elif operation == '-':
        result = round(x - y, precision)
    elif operation == '*':
        result = round(x * y, precision)
    elif operation == '/' and y != 0:
        result = round(x / y, precision)
    elif operation == '/' and y == 0:
        return "Деление на ноль невозможно!"
    else:
        return "Некорректная операция!"

    return result


def main():
    """Основная функция, которая запрашивает ввод данных у пользователя
    и выводит результат вычисления.
    Запрашивает у пользователя два числа и операцию, затем вызывает
    функцию calculate и выводит результат.
    """
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    operation = input("Выберите действие ('+', '-', '*', '/'): ")

    try:
        result = calculate(x, y, operation)
        print(result)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
