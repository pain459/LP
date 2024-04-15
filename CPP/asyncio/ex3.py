# async programming -- submitting tasks in the background

import asyncio
import time


async def func1():
    task = asyncio.create_task(asyncio.sleep(3))
    print('From func1')
    # await task
    # await asyncio.sleep(3)


async def func2():
    print('From func2')
    await asyncio.sleep(2)


async def func3():
    print('From func3')
    await asyncio.sleep(1)


def main():
    start_time = time.perf_counter()
    asyncio.run(func1())
    asyncio.run(func2())
    asyncio.run(func3())
    end_time = time.perf_counter()
    print(f'Program took {round(end_time - start_time, 2)} second(s).')


if __name__ == "__main__":
    main()
