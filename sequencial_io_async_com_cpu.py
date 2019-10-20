import asyncio
from concurrent import futures
import aiohttp
import time

    
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def do_request():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.co.uk')
      

async def slow_function():  
    loop = asyncio.get_running_loop()
    await do_request()
    with futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool,
                    pow, 9, 999999)
    return result



def main():
    t0 = time.perf_counter()

    repeted_requests = [slow_function() for i in range(200)]
    loop = asyncio.get_event_loop()
    repeted_requests = asyncio.gather(*repeted_requests)
    loop.run_until_complete(repeted_requests)
    dt = time.perf_counter() - t0
    print(f"Elapsed time : {dt:0.3}s")


if __name__ == '__main__':
    main()
