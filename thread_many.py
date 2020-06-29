from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import asyncio
import aiohttp
import os

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def do_request(number):
    async with aiohttp.ClientSession() as session:
        text = await fetch(session, 'http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.google.co.uk')
        print(number)


async def main(number):
    tasks = [do_request(number) for i in range(3)]
    await asyncio.gather(*tasks)
            

class Thereadinha(Thread):
    def __init__(self, number):
        Thread.__init__(self)
        self.daemon = True
        self.number = number
        self.start()

    def run(self):
        loop = asyncio.new_event_loop()
        while True:
            loop.run_until_complete(main(self.number))
            


[Thereadinha(i) for i in range(os.cpu_count())]
while True:
    pass