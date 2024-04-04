import os
import time
import asyncio
from datetime import datetime

COEFF = 0.01


async def talk(name, prepare, def_prepare, end, def_end):
    print(f"{name} started the 1 task.")
    await asyncio.sleep(COEFF * prepare)
    print(f"{name} started the 2 task.")
    await asyncio.sleep(COEFF * end)
    print(f"{name} moved on to the defense of the 1 task.")
    await asyncio.sleep(COEFF * def_prepare)
    print(f'{name} completed the 1 task.')
    print(f"{name} moved on to the defense of the 2 task.")
    await asyncio.sleep(COEFF * def_end)
    print(f'{name} completed the 2 task.')
    await asyncio.sleep(COEFF * end)


async def interviews(*data):
    tasks = []
    for i in data:
        tasks.append(asyncio.create_task(talk(*i)))
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)
