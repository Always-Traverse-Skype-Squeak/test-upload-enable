import pytest
from fibonacci import recursive_fibonacci

@pytest.mark.benchmark(group="Recursive Fibo")
def test_recursive_fibo_10(benchmark):
    @benchmark
    def _():
        recursive_fibonacci(10)


@pytest.mark.benchmark(group="Recursive Fibo")
def test_recursive_fibo_20(benchmark):
    @benchmark
    def _():
        recursive_fibonacci(20)
