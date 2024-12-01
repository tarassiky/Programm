def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def ten_to_fib(fibonacci_gen):
    for number in fibonacci_gen:
        yield number + 10

def main():
    fibonacci_seq_gen = fibonacci_generator()
    modified_fib_gen = ten_to_fib(fibonacci_seq_gen)

    count = 8  # Увеличенный диапазон для генерации чисел Фибоначчи

    for _ in range(count):
        print(next(modified_fib_gen))

if __name__ == "__main__":
    main()
