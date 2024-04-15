# Basic example of asyncio based program.
# Using await and asyncio

import asyncio


async def main():
    print('This is running.')
    await foo('Sample')


async def foo(text):
    print(text)
    await asyncio.sleep(1.5)
    print('Sleep completed.')
    print(text)


asyncio.run(main())
