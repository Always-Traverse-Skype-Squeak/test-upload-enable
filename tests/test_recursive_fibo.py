from fibonacci import recursive_fibonacci


def test_recursive_fibo_10(benchmark):
    @benchmark
    def _():
        recursive_fibonacci(10)


def test_recursive_fibo_20(benchmark):
    @benchmark
    def _():
        recursive_fibonacci(20)
