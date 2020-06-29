import asyncio
import time

loop = asyncio.get_event_loop()

import time


async def cozinha_macarrao(number):
    print(f"Preparando macarrão {number}")
    await asyncio.sleep(15)
    print(f"Macarrão pronto {number}")


async def pegar_macarrao(number):
    await asyncio.sleep(3)
    print(f"Pegando macarrão para cozinha {number}")


async def check_tasks(tasks):
    while True:
        if all(task.done() for task in tasks):
            print("todas tasks finalizadas")
            loop.stop()
        await asyncio.sleep(0.1)


async def main():
    tasks = []
  
    for i in range(1, 3):
        await pegar_macarrao(i)
        task = loop.create_task(cozinha_macarrao(i))
        tasks.append(task)
    await check_tasks(tasks)




loop.create_task(main())

t0 = time.perf_counter()

loop.run_forever()


dt = time.perf_counter() - t0
print(f"Finished in : {dt:0.3}s")