import time

class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end_time = time.perf_counter()
        self.duration = self.end_time - self.start_time
        print(f"Время выполнения: {self.duration:.6f} секунд.")

def generate_fibonacci(z):
    x, y = 0, 1
    for i in range(z):
        yield x
        x, y = y, x + y

def main():
    z = 1000000
    with Timer():
        for i in generate_fibonacci(z):
            pass

if __name__ == "__main__":
    main()





