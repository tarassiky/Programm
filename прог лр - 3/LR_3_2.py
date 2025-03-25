import sys
import functools
import sqlite3
import json
from datetime import datetime
from contextlib import contextmanager


# Функция-декоратор
def trace(func=None, *, handle=sys.stdout):
    if func is None:
        return lambda func: trace(func, handle=handle)

    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)

            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = {
                'datetime': now,
                'func_name': func.__name__,
                'params': args,
                'result': result
            }

            if isinstance(handle, str) and handle.endswith('.json'):
                with open(handle, 'a+') as file:
                    json.dump(data, file, indent=4)
                    file.write('\n')
            elif isinstance(handle, sqlite3.Connection):
                # Внутри декоратора создаем таблицу, если она не существует
                cursor = handle.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS logtable (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        datetime TEXT,
                        func_name TEXT,
                        params TEXT,
                        result TEXT
                    )
                ''')
                cursor.execute('''
                    INSERT INTO logtable(datetime, func_name, params, result) 
                    VALUES (?, ?, ?, ?)
                ''', (now, func.__name__, str(args), str(result)))
                handle.commit()
            else:
                handle.write(f'{data}\n')

            return result
        except Exception as e:
            raise e

    return inner


@contextmanager
def dbc(filename=":memory:"):
    """
    Контекстный менеджер для подключения к базе данных SQLite.
    По умолчанию подключаемся к базе данных в памяти.
    Можно передать путь к файлу базы данных.
    """
    con = sqlite3.connect(filename)
    try:
        yield con
    finally:
        con.close()


@trace(handle=sys.stderr)
def increase(x):
    """Увеличивает число на 1."""
    return x + 1


@trace(handle='logger.json')
def decrease(x):
    """Уменьшает число на 1."""
    return x - 1


@trace(handle='log_data.json')
def power_of_three(x):
    return x ** 3


def main():
    with dbc("example.db") as con:
        @trace(handle=con)
        def power_of_four(x):
            return x ** 4

        increase(5)
        decrease(12)
        power_of_three(4)
        power_of_four(7)

        cursor = con.cursor()
        cursor.execute('SELECT * FROM logtable')
        for row in cursor.fetchall():
            print(row)

        # Вызов функции power_of_four внутри блока with
        print(power_of_four(10))


if __name__ == "__main__":
    main()
