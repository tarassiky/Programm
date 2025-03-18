import sys
import functools
import sqlite3
import json
from datetime import datetime


#  Декоратор для отслеживания вызовов функций
def call_tracer(func=None, *, log_destination=sys.stdout):
    """
    Параметризованный декоратор для логирования вызовов функций.
    """
    print("func - > ", func)
    if func is None:
        return lambda func: call_tracer(func, log_destination=log_destination)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_data = {
                'timestamp': timestamp,
                'function_name': func.__name__,
                'parameters': args,
                'outcome': result
            }

            if isinstance(log_destination, str) and log_destination.endswith('.json'):
                with open(log_destination, 'a+') as log_file:
                    json.dump(log_data, log_file, indent=4)
                    log_file.write('\n')
            elif isinstance(log_destination, sqlite3.Connection):
                cursor = log_destination.cursor()
                cursor.execute('''INSERT INTO function_log(timestamp, function_name, parameters, outcome) 
                                  VALUES (?, ?, ?, ?)''',
                               (timestamp, func.__name__, str(args), str(result)))
                log_destination.commit()
            else:
                log_destination.write(f'{log_data}\n')

            return result

        except Exception as error:
            print(f"An error occurred in {func.__name__}: {error}")
            raise

    return wrapper


# Создание таблицы для логов в базе данных SQLite
def setup_log_table(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS function_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            function_name TEXT,
            parameters TEXT,
            outcome TEXT
        )
    ''')
    connection.commit()


# Вывод логов из базы данных SQLite
def display_logs(connection: sqlite3.Connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM function_log')
    log_records = cursor.fetchall()
    for record in log_records:
        print(record)


# Примеры использования:

@call_tracer(log_destination=sys.stderr)  # Логирование в stderr
def increase(x):
    """Увеличивает число на 1."""
    return x + 1


@call_tracer(log_destination=sys.stdout)  # Логирование в stdout
def decrease(x):
    """Уменьшает число на 1."""
    return x - 1


@call_tracer(log_destination='log_data.json')  # Логирование в JSON-файл
def power_of_three(x):
    return x ** 3


# Инициализация базы данных SQLite в памяти
db_conn = sqlite3.connect(':memory:')
setup_log_table(db_conn)


@call_tracer(log_destination=db_conn)
def power_of_four(x):
    return x ** 4


# Пример добавления данных в базу данных
cursor = db_conn.cursor()
cursor.execute("INSERT INTO function_log (timestamp, function_name, parameters, outcome) VALUES ('2024-01-01', 'example', '2', '4')")
db_conn.commit()

# Вызовы функций
increase(5)  # Изменено значение
decrease(12) # Изменено значение
power_of_three(4) # Изменено значение
power_of_four(7) # Изменено значение

# Вывод логов из базы данных
display_logs(db_conn)

# Закрытие соединения с базой данных
db_conn.close()