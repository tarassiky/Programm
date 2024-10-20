# 2 задание
import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def log_decorator(function):
    def wrapper(x, y, operation):
        logger.info(f'Введенные операнды и операция: {x}, {y}, {operation}')
        result = function(x, y, operation)
        logger.info("Результат: %s.", result)
        return result

    return wrapper
    """
    Декоратор, который логирует вызовы функций.
    """

@log_decorator
def calculate(x, y, operation):
    """
    Вычисление результата операции.
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

def test_calculate():
    """
    Тесты.
    """
    assert calculate(9, 3, "+") == 12
    assert calculate(7, 4, "-") == 3
    assert calculate(6, 4, "*") == 24
    assert calculate(8, 2, "/") == 4
    assert calculate(2, 0, "/") == "Деление на ноль невозможно!"

def main():
    """
    Основная функция.
    """
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    operation = input("Выберите действие ('+', '-', '*', '/'): ")
    result = calculate(x, y, operation)
    print(result)

if __name__ == "__main__":
    main()
