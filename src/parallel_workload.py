"""Workloads used by the multi-threaded / multi-process benchmarks.

These are intentionally CPU-bound so that running them across several
processes or threads produces measurable, parallelizable work.
"""

from fibonacci import recursive_fibonacci


def fibo_workload(n: int) -> int:
    """A CPU-bound unit of work shared by the parallel benchmarks."""
    return recursive_fibonacci(n)
