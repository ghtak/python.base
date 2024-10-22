from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

import aiohttp
import psutil


def mem_usage():
    p = psutil.Process()
    print(f'mem usage : {p.memory_info().rss / 2 ** 20}MB')


def fetch(uid):
    resp = requests.get(f'http://0.0.0.0:3111/{uid}')
    return resp.json()


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=20) as executor:
        futs = [executor.submit(fetch, i) for i in range(0, 100)]
        for fut in as_completed(futs):
            mem_usage()
            print(fut.result())
