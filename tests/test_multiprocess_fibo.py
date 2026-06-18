"""Multi-process benchmark: at least two processes, one thread per process.

Each worker process runs the CPU-bound fibonacci workload on its own,
single main thread. This exercises CodSpeed's handling of benchmarks that
fork multiple OS processes.
"""

from concurrent.futures import ProcessPoolExecutor

import pytest

from parallel_workload import fibo_workload

# At least two processes, one (main) thread each.
N_PROCESSES = 4
FIBO_N = 28


def _run_across_processes() -> list[int]:
    with ProcessPoolExecutor(max_workers=N_PROCESSES) as executor:
        results = list(executor.map(fibo_workload, [FIBO_N] * N_PROCESSES))
    return results


@pytest.mark.walltime_only
@pytest.mark.benchmark(group="Parallel Fibo")
def test_multiprocess_fibo(benchmark):
    @benchmark
    def _():
        _run_across_processes()
