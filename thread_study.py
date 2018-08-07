import asyncio
from concurrent.futures import ThreadPoolExecutor
def func(a, b):
    # Do time intensive stuff...
    return a + b


async def main(loop):
    executor = ThreadPoolExecutor()
    result = await loop.run_in_executor(executor, func, "Hello,", " world!")
    print(result)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))