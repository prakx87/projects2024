import asyncio
import json
import time

import aiohttp

async def worker(name, n, session):
    print(f"worker-{name}")
    url = f"https://www.randomnumberapi.com/api/v1.0/random?min=100&max=1000&count={n}"
    response = await session.request(method="GET", url=url)
    value = await response.text()
    value = json.loads(value)
    return sum(value)

async def main():
    async with aiohttp.ClientSession() as session:
        sums = await asyncio.gather(*(worker(f"w{i}", n, session) for i, n in enumerate(range(2, 30))))
        print(f"sums: {sums}")


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Executed in {elapsed:0.2f} seconds.")
