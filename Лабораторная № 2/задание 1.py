# Задание 1
def book():
    """
        Функция book, возвращает информацию о книге, т.е. вложенную функцию inner_book

        :param name: int название
        :param year: str год
        :param author: str автор

    """

    name = 'Ночь в Лиссабоне'
    year = 1961
    author = 'Эрих Мария Ремарк'

    def inner_book():
        """
            возвращает словарь с данными о книге

            :param name: int название
            :param year: str год
            :param author: str автор

        """
        return {'name': name, 'year': year, 'author': author}

    return inner_book()


print(book())
