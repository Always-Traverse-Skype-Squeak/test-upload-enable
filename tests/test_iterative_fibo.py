import pytest
from fibonacci import iterative_fibonacci


@pytest.mark.benchmark(group="Iterative Fibo")
@pytest.mark.parametrize("n", [10, 25])
def test_iterative_fibo(benchmark, n):
    @benchmark
    def _():
        iterative_fibonacci(n)
