import logging

# Настройка логирования
logger = logging.getLogger("Calculator")
logging.basicConfig(level=logging.INFO)

def log_decorator(function):
    """
    Декоратор, который логирует вызовы функций.

    :param function: Функция, которую необходимо обернуть логированием.
    :return: Обернутая функция с логированием.
    """
    def wrapper(x, y, operation):
        logger.info(f'Введенные операнды и операция: {x}, {y}, {operation}')
        result = function(x, y, operation)
        logger.info("Результат: %s.", result)
        return result

    return wrapper

@log_decorator
def calculate(x, y, operation):
    """
    Вычисление результата операции.

    :param x: Первое число.
    :param y: Второе число.
    :param operation: Операция для выполнения ('+', '-', '*', '/').
    :return: Результат вычисления или сообщение об ошибке при делении на ноль.
    """
    if operation == '+':
        return x + y
    elif operation == '-':
        return x - y
    elif operation == '*':
        return x * y
    elif operation == '/' and y != 0:
        return x / y
    elif operation == '/' and y == 0:
        return "Деление на ноль невозможно!"
    else:
        return "Некорректная операция!"

# def test_calculate():
#     """
#     Тесты для функции calculate.
#
#     Проверяет корректность работы функции calculate с различными операциями.
#     """
#     assert calculate(9, 3, "+") == 12.0
#     assert calculate(7, 4, "-") == 3.0
#     assert calculate(6, 4, "*") == 24.0
#     assert calculate(8, 2, "/") == 4.0
#     assert calculate(2, 0, "/") == "Деление на ноль невозможно!"
#     assert calculate(2, 3, "^") == "Некорректная операция!"  # Тест на некорректную операцию

def main():
    """
    Основная функция, которая запрашивает ввод данных у пользователя
    и выводит результат вычисления.

    Запрашивает у пользователя два числа и операцию, затем вызывает
    функцию calculate и выводит результат.
    """
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    operation = input("Выберите действие ('+', '-', '*', '/'): ")
    result = calculate(x, y, operation)
    print(result)

if __name__ == "__main__":
    main()
