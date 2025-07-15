import pytest
from fibonacci import iterative_fibonacci


@pytest.mark.benchmark(group="Iterative Fibo")
def test_iterative_fibo_10(benchmark):
    @benchmark
    def _():
        iterative_fibonacci(10)

@pytest.mark.benchmark(group="Iterative Fibo")
def test_iterative_fibo_25(benchmark):
    @benchmark
    def _():
        iterative_fibonacci(25)
