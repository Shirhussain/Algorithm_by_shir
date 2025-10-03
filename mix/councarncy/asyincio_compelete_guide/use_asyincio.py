
# https://superfastpython.com/python-asyncio-jump-start/
# for more advance go her: https://superfastpython.com/python-asyncio-jump-start/
# trade blocking:  https://superfastpython.com/thread-blocking-call-in-python/
import asyncio
# define a custom coroutine in Python 3.4


async def some_function():
    await asyncio.sleep(2)


async def main():
    await some_function()

asyncio.run(main())
