import random


class RandomIntegerGenerator:
    def __init__(self, settings: list):
        self.settings = settings
        self.total_numbers = settings[0]  # Общее количество чисел для генерации
        self.lower_bound = settings[1]     # Нижняя граница диапазона
        self.upper_bound = settings[2]     # Верхняя граница диапазона
        self.generated_list = []            # Список для сгенерированных чисел

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.generated_list) < self.total_numbers:
            random_number = random.randint(self.lower_bound, self.upper_bound)
            self.generated_list.append(random_number)
            return random_number
        else:
            raise StopIteration

    def get_settings(self):
        return self.settings


def main():
    # Задаем параметры: общее количество чисел, нижняя и верхняя граница
    num_generator = RandomIntegerGenerator([7, 15, 100])  # Измененный диапазон

    # Используем цикл for для вывода всех сгенерированных чисел
    for value in num_generator:
        print(value)


if __name__ == "__main__":
    main()
