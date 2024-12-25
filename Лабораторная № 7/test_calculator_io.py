import pytest
import os
import json
from ex_onee import load_params, write_log

def test_load_params_success(tmpdir):
    """Тестирует успешную загрузку параметров из JSON-файла."""
    params_file = tmpdir.join("test_params.json")
    params_file.write('{"precision": 0.0001, "dest": "test_output.txt"}')
    loaded_params = load_params(str(params_file))
    assert loaded_params["precision"] == 0.0001
    assert loaded_params["dest"] == "test_output.txt"

def test_load_params_value_error(tmpdir):
    """Тестирует обработку ValueError при некорректном JSON."""
    params_file = tmpdir.join("bad_params.json")
    params_file.write('{"precision": 0.0001, "dest": test_output.txt}')  # Некорректный JSON
    with pytest.raises(ValueError, match="Ошибка при парсинге JSON"):
        load_params(str(params_file))

def test_write_log_success_new_file(tmpdir):
    """Тестирует запись лога в новый файл."""
    log_file = tmpdir.join("test_log.txt")
    write_log(1, 2, action="test", result=3, file_path=str(log_file))
    with open(str(log_file), "r") as f:
        content = f.read()
    assert "test: (1, 2) = 3" in content

def test_write_log_success_append_file(tmpdir):
    """Тестирует добавление записи в существующий файл лога."""
    log_file = tmpdir.join("test_log.txt")
    with open(str(log_file), "w") as f:
        f.write("Initial content\n")
    write_log(4, 5, action="add", result=9, file_path=str(log_file))
    with open(str(log_file), "r") as f:
        content = f.read()
    assert "Initial content\nadd: (4, 5) = 9" in content

def test_write_log_permission_error(tmpdir):
    """Тестирует обработку ошибки записи в файл при отсутствии прав."""
    # Создаем недопустимый путь для теста
    invalid_path = '/invalid_path/test_log.txt'
    with pytest.raises(Exception, match="Ошибка записи в файл"):
        write_log(1, 2, action='test', result=3, file_path=invalid_path)

def test_write_log_file_not_found(tmpdir):
    """Тестирует запись лога в несуществующий файл."""
    log_file = tmpdir.join("non_existent_log.txt")
    write_log(6, 7, action="create", result=13, file_path=str(log_file))
    assert os.path.exists(str(log_file))
    with open(str(log_file), "r") as f:
        content = f.read()
    assert "create: (6, 7) = 13" in content
