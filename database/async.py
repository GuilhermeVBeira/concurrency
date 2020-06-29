import asyncio
import asyncpg
import string
import random
import time



def random_string(string_length=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(string_length))


async def insert_many(conn):
    tasks = [(i, random_string()) for i in range(600000)]
    return await conn.copy_records_to_table("role", records=tasks)


async def main():

    t0 = time.perf_counter()
    conn = await asyncpg.connect(
        "postgresql://async_test:async_test@localhost/async_test"
    )
    result = await insert_many(conn)
    print(result)
    await conn.close()
    dt = time.perf_counter() - t0
    print(f"Finished in : {dt:0.3}s")



asyncio.run(main())
