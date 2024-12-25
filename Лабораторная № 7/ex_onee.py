import json
import os

DEFAULT_PARAMS = {'precision': 0.00001, 'dest': 'output.txt'}

def load_params(file_path="params.json"):
    """Загружает параметры из JSON-файла и обновляет значения по умолчанию.

    Аргументы:
        file_path (str): Путь к файлу параметров.

    Возвращает:
        dict: Загруженные параметры, включая значения по умолчанию.

    Поднимает:
        ValueError: Если файл содержит некорректный JSON.
    """
    global DEFAULT_PARAMS
    try:
        with open(file_path, mode='r', errors='ignore') as f:
            try:
                loaded_params = json.load(f)
                DEFAULT_PARAMS.update(loaded_params)
            except json.JSONDecodeError as e:
                raise ValueError(f"Ошибка при парсинге JSON: {e}") from e
    except FileNotFoundError:
        print(f"Файл параметров '{file_path}' не найден, используются значения по умолчанию.")
    return DEFAULT_PARAMS

def write_log(a, b, action, result, file_path='calc-history.log.txt'):
    """Записывает лог операции в файл.

    Аргументы:
        a (int): Первое число.
        b (int): Второе число.
        action (str): Операция ('add', 'subtract', 'multiply', 'divide').
        result (float): Результат операции.
        file_path (str): Путь к файлу лога.
    """
    try:
        with open(file_path, mode='a', errors='ignore') as f:
            f.write(f"{action}: ({a}, {b}) = {result}\n")
    except FileNotFoundError as e:
        raise Exception(f'Ошибка записи в файл {file_path}: {e}') from e

def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    elif operation == '*':
        return a * b
    else:
        raise ValueError("Неизвестная операция")
