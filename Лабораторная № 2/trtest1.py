from tr import calculate

def test_calculate1():
    """
    Тесты для функции calculate.

    Проверяет корректность работы функции calculate с различными операциями.
    """
    assert calculate(9, 3, "+") == 12.0
test_calculate1()

def test_calculate2():

    assert calculate(7, 4, "-") == 3.0
test_calculate2()

def test_calculate3():

    assert calculate(6, 4, "*") == 24.0
test_calculate3()

def test_calculate4():

    assert calculate(8, 2, "/") == 4.0
test_calculate4()

def test_calculate5():

    assert calculate(2, 0, "/") == "Деление на ноль невозможно!"
test_calculate5()

def test_calculate6():

    assert calculate(2, 3, "^") == "Некорректная операция!"  # Тест на некорректную операцию
test_calculate6()