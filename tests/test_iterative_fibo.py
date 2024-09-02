from fibonacci import iterative_fibonacci


def test_iterative_fibo_10(benchmark):
    @benchmark
    def _():
        iterative_fibonacci(10)
