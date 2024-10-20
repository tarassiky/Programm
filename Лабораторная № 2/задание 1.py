#Задание 1
def book():

    name = 'Ночь в Лиссабоне'
    year = 1961
    author = 'Эрих Мария Ремарк'

    def inner_book():

        return{'name': name, 'year': year, 'author': author}


    return inner_book()

print(book())
