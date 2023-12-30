from random import randint
import time
import asyncio


def odds(start, stop):
    for odd in range(start, stop + 1, 2):
        yield odd


async def randn():
    await asyncio.sleep(3)
    return randint(1, 10)


async def main():
    odd_values = [odd for odd in odds(3, 15)]
    odds2 = tuple(odds(21, 29))
    print(odd_values)
    print(odds2)

    start = time.perf_counter()
    r = await randn()
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds")

    start = time.perf_counter()
    r = await asyncio.gather(*(randn() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed:0.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())