import pytest
import os
from LR66 import write_log, calculate

def test_file_creation_exception():
    parameters = [9, 3]
    log_file_path = 'newoutput2.txt'
    with pytest.raises(Exception) as exc_info:
        write_log(*parameters, action='*', file=log_file_path)
    assert "Ошибка записи в файл" in str(exc_info.value)

def test_calculate_zero_division():
    parameters = [9, 0]
    expected_message = "Деление на ноль невозможно"
    with pytest.raises(ValueError, match=expected_message):
        calculate(*parameters, operation='/')

def test_successful_log_write():
    log_file_name = "log_test.txt"
    try:
        write_log(5, 3, action="add", result=8, file=log_file_name)
        with open(log_file_name, "r") as file:
            content = file.read()
        assert "add: (5, 3) = 8" in content
    finally:
        if os.path.exists(log_file_name):
            os.remove(log_file_name)
