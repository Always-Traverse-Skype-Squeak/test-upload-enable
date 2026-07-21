import sys

import pytest

from fibonacci import recursive_cached_fibonacci

sys.setrecursionlimit(200000)


@pytest.mark.benchmark(group="Recursive Fibo Cached - small n")
@pytest.mark.parametrize("n", [10, 100])
def test_recursive_cached_fibo_small(benchmark, n):
    @benchmark
    def _():
        recursive_cached_fibonacci(n)


@pytest.mark.benchmark(group="Recursive Fibo Cached - large n")
@pytest.mark.parametrize("n", [1000])
def test_recursive_cached_fibo_large(benchmark, n):
    @benchmark
    def _():
        recursive_cached_fibonacci(n)
