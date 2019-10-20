import aiohttp
import asyncio
import time


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def do_request():
    pow(9, 999999)
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.co.uk')
        

if __name__ == '__main__':
    t0 = time.perf_counter()
    repeted_requests = [do_request() for i in range(200)]
    loop = asyncio.get_event_loop()
    repeted_requests = asyncio.gather(*repeted_requests)
    loop.run_until_complete(repeted_requests)
    dt = time.perf_counter() - t0
    print(f"Elapsed time : {dt:0.3}s")