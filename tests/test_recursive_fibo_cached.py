import sys

from fibonacci import recursive_cached_fibonacci

sys.setrecursionlimit(200000)


def test_recursive_cached_fibo_10(benchmark):
    @benchmark
    def _():
        recursive_cached_fibonacci(10)


def test_recursive_cached_fibo_100(benchmark):
    @benchmark
    def _():
        recursive_cached_fibonacci(100)


def test_recursive_cached_fibo_1000(benchmark):
    @benchmark
    def _():
        recursive_cached_fibonacci(1000)
