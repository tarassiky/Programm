PARAMS = {'precision': 0.00001, 'dest': 'newoutput.txt'}


def load_params(file="params.ini"):
    global PARAMS
    try:
        with open(file, mode='r', errors='ignore') as f:
            lines = f.readlines()
            for l in lines:
                param = l.strip().split('=')
                if len(param) == 2:
                    key, value = param
                    key = key.strip()
                    value = value.strip()
                    if key != 'dest':
                        try:
                            value = eval(value)
                        except Exception as e:
                            print(f"Ошибка при парсинге значения '{value}' для параметра {key}: {e}")
                            continue
                    PARAMS[key] = value
    except FileNotFoundError:
        print(f"Файл параметров '{file}' не найден, используются значения по умолчанию.")
    return PARAMS


def write_log(*args, action=None, result=None, file='calc-history.log.txt'):
    error = None
    try:
        with open(file, mode='a', errors='ignore') as f:
            f.write(f"{action}: {args} = {result} \n")
    except PermissionError:
        print(f'Ошибка записи в файл {file}')
        file_new = file + '.txt'
        print(f'Попытка записать лог в файл с новым именем: {file_new}')
        try:
            with open(file_new, mode='a', errors='ignore') as backup_file:
                backup_file.write(f"{action}: {args} = {result} \n")
        except PermissionError as e:
            error = e

    if error:
        raise Exception(
            f'Ошибка записи в файл {file_new}. Записать не удалось.')


def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        if b == 0:
            raise ValueError("Division by zero is not possible")
        return a / b
    elif operation == '*':
        return a * b
    else:
        raise ValueError("Unknown operation")


def main():
    load_params()
    print(f"Загруженные параметры: {PARAMS}")

    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        operation = input("Введите операцию (+, -, /, *): ")

        result = calculate(a, b, operation)
        print(f"Результат: {result}")

        try:
            write_log(a, b, action=operation, result=result, file=PARAMS['dest'])
        except Exception as e:
            print(f"Ошибка записи в лог: {e}")
            print(f"Не удалось записать в лог: {operation}: ({a}, {b}) = {result}")
            try:
                write_log(
                    f"Ошибка логирования: {e}",
                    action="error",
                    file='calc-history.log.txt'
                 )
            except Exception as log_e:
                print(f"Критическая ошибка! Не удалось записать ошибку в {file}. Ошибка: {log_e}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()