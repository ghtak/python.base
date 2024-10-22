import asyncio

import aiohttp
import psutil


def mem_usage():
    p = psutil.Process()
    print(f'mem usage : {p.memory_info().rss / 2 ** 20}MB')


async def fetch(session, uid):
    async with session.get(f'http://0.0.0.0:3111/{uid}') as response:
        json_value = await response.json()
        mem_usage()
        # print(f'{json_value}')


async def hello_asyncio():
    connector = aiohttp.TCPConnector(limit=1000)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [asyncio.create_task(fetch(session, i)) for i in range(0, 1000)]
        mem_usage()
        await asyncio.gather(*tasks)
        mem_usage()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(hello_asyncio())
