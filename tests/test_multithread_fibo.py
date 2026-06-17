"""Multi-thread benchmark: a single process running multiple threads.

The CPU-bound fibonacci workload is dispatched across several threads
within one process. This exercises CodSpeed's handling of benchmarks
that spawn multiple threads in the same process.
"""

from concurrent.futures import ThreadPoolExecutor

import pytest

from parallel_workload import fibo_workload

# Multiple threads within a single process.
#
# FIBO_N is sized so the exponential `recursive_fibonacci` work dominates the
# wall time: the computation must eclipse the thread-pool setup/teardown system
# calls, otherwise the syscall overhead drowns out the work and the profiler
# can't build a flamegraph. ~0.7s of compute keeps it well above the
# sub-millisecond syscall floor while staying reasonably quick.
N_THREADS = 4
FIBO_N = 31


def _run_across_threads() -> list[int]:
    with ThreadPoolExecutor(max_workers=N_THREADS) as executor:
        results = list(executor.map(fibo_workload, [FIBO_N] * N_THREADS))
    return results


@pytest.mark.benchmark(group="Parallel Fibo")
def test_multithread_fibo(benchmark):
    @benchmark
    def _():
        _run_across_threads()
