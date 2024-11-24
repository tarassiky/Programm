def fib(n):
    mem = {0: 0, 1: 1}

    def f(n):
        if n not in mem:
            mem[n] = f(n - 1) + f(n - 2)
        return mem[n]

    return f(n)

print(fib(6))

from functools import cache

@cache
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)

print(fib_cached(6))