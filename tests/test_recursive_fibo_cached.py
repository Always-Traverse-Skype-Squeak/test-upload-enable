import sys

import pytest

from fibonacci import recursive_cached_fibonacci

sys.setrecursionlimit(200000)


@pytest.mark.benchmark(group="Recursive Fibo Cached")
@pytest.mark.parametrize("n", [10, 100, 1000])
def test_recursive_cached_fibo(benchmark, n):
    @benchmark
    def _():
        recursive_cached_fibonacci(n)
