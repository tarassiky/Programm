import logging
import math
import statistics

# Настройка логирования
logger = logging.getLogger("Calculator")
logging.basicConfig(level=logging.INFO)


def log_decorator(function):
    """Декоратор, который логирует вызовы функций.
    :param function: Функция, которую необходимо обернуть логированием.
    :return: Обернутая функция с логированием.
    """

    def wrapper(*args, **kwargs):
        logger.info(f'Введенные аргументы: {args}, {kwargs}')
        result = function(*args, **kwargs)
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
def calculate(action, *args, tolerance=1e-6):
    """
    Вычисление результата операции.
    :param action: Операция для выполнения ('+', '-', '*', '/', 'medium', 'variance', 'std_deviation', 'median', 'iqr').
    :param args: Переменное количество операндов.
    :param tolerance: Значение для определения точности округления.
    :return: Результат вычисления или сообщение об ошибке.
    """
    try:
        precision = convert_precision(tolerance)
    except ValueError as e:
        raise ValueError(f"Ошибка в параметре tolerance: {e}")

    if action == '+':
        result = round(sum(args), precision)
    elif action == '-':
        result = round(args[0] - sum(args[1:]), precision)
    elif action == '*':
        result = round(math.prod(args), precision)
    elif action == '/':
        if len(args) < 2 or any(y == 0 for y in args[1:]):
            return "Деление на ноль невозможно!"
        result = round(args[0] / math.prod(args[1:]), precision)
    elif action == 'medium':
        result = round(statistics.mean(args), precision)
    elif action == 'variance':
        result = round(statistics.variance(args), precision)
    elif action == 'std_deviation':
        result = round(statistics.stdev(args), precision)
    elif action == 'median':
        result = round(statistics.median(args), precision)
    elif action == 'iqr':
        q1 = statistics.quantiles(args, n=4)[0]
        q3 = statistics.quantiles(args, n=4)[2]
        result = round(q3 - q1, precision)
    else:
        return "Некорректная операция!"

    return result


def main():
    """Основная функция, которая запрашивает ввод данных у пользователя
    и выводит результат вычисления.
    Запрашивает у пользователя операцию и операнды, затем вызывает
    функцию calculate и выводит результат.
    """
    operation = input(
        "Выберите действие ('+', '-', '*', '/', 'medium', 'variance', 'std_deviation', 'median', 'iqr'): ")

    # Запрос аргументов
    args = input("Введите операнды через запятую: ")
    args = [float(x) for x in args.split(",")]

    try:
        result = calculate(operation, *args)
        print(result)
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
