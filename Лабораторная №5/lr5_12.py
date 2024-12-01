import random

def generate_random_integers(count, low, high):
    """Генератор случайных целых чисел в данном диапазоне."""
    for i in range(count):
        yield random.randint(low, high)

def main():
    # Указываем параметры: количество чисел, нижняя и верхняя границы
    total_numbers = 10  # Теперь генерируется 10 чисел
    lower_bound = 20    # Нижняя граница диапазона
    upper_bound = 200   # Верхняя граница диапазона

    # Используем цикл for для вывода всех сгенерированных чисел
    for number in generate_random_integers(total_numbers, lower_bound, upper_bound):
        print(number)

if __name__ == "__main__":
    main()
