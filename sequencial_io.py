import requests
import time

t0 = time.perf_counter()

for i in range(10):
    requests.get("http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.co.uk")

dt = time.perf_counter() - t0
print(f"Elapsed time : {dt:0.3}s")