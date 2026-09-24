import pytest
from fibonacci import recursive_fibonacci


@pytest.mark.benchmark(group="Recursive Fibo")
@pytest.mark.parametrize("n", [10, 20])
def test_recursive_fibo(benchmark, n):
    @benchmark
    def _():
        recursive_fibonacci(n + 2)
