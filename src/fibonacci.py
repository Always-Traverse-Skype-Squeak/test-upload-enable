def recursive_fibonacci(n: int) -> int:
    if n in [0, 1]:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


def recursive_cached_fibonacci(n: int) -> int:
    cache = {0: 0, 1: 1}

    def fibo(n) -> int:
        if n in cache:
            return cache[n]
        cache[n] = fibo(n - 1) + fibo(n - 2)
        return cache[n]

    return fibo(n)


def iterative_fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
