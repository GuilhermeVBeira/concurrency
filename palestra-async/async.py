import asyncio
import time


async def cozinha_macarrao(number):
    print(f"Preparando macarrão {number}")
    await asyncio.sleep(15)
    print(f"Macarrão pronto {number}")


async def pegar_macarrao(number):
    await asyncio.sleep(3)
    print(f"Pegando macarrão para cozinha {number}")


async def main():
    t0 = time.perf_counter()
    tasks = []
    t0 = time.perf_counter()
    for i in range(1, 3):
        import pdb; pdb.set_trace()
        await pegar_macarrao(i)
        task = asyncio.create_task(cozinha_macarrao(i), name=f"Cozinando macarrao {i}")
        tasks.append(task)
    await asyncio.gather(*tasks)
    dt = time.perf_counter() - t0
    print(f"Finished in : {dt:0.3}s")


asyncio.run(main())
