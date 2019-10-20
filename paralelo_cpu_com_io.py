import concurrent.futures
import time
from multiprocessing.context import ForkContext
t0 = time.perf_counter()
results = []

def calcula():
    return pow(9, 999999)

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Start the load operations and mark each future with its URL
    future_to_pow = {executor.submit(calcula): i for i in range(150)}
    for future in concurrent.futures.as_completed(future_to_pow):
        task_number = future_to_pow[future]
        # print(f"tarefa {task_number} finalizada")
        try:
            results.append(future.result())
        except Exception as exc:
            print(f'Generated an exception: {exc}')

dt = time.perf_counter() - t0
print(f"Elapsed time : {dt:0.3}s")
