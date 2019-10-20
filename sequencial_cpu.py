import time

t0 = time.perf_counter()

for i in range(100):
    pow(9, 999999)

dt = time.perf_counter() - t0
print(f"Elapsed time : {dt:0.3}s")