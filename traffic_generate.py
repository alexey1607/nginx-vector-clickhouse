#!/usr/bin/env python3

import asyncio
import random
import argparse
import aiohttp
import json

DEFAULT_LOCATIONS = ["/", "/health", "/msk", "/spb", "/ekb", "/vlgd"]

USER_AGENTS = [
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0",
    "curl/8.5.0",
    "k6/0.48.0",
    "python-aiohttp/3.x",
]


def parse_locations(value: str):
    try:
        locations = json.loads(value)
        if not isinstance(locations, list):
            raise ValueError("locations must be a JSON array")
        return locations
    except json.JSONDecodeError as e:
        raise argparse.ArgumentTypeError(
            f"Invalid JSON for locations: {e}"
        )


async def fetch(session: aiohttp.ClientSession, url: str, sem: asyncio.Semaphore, idx: int):
    async with sem:
        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }

        try:
            async with session.get(url, headers=headers) as response:
                status = response.status
                await response.text()
                print(f"[{idx}] {url} -> {status}")
        except Exception as e:
            print(f"[{idx}] {url} -> ERROR: {e}")


async def run(args):
    sem = asyncio.Semaphore(args.concurrency)
    timeout = aiohttp.ClientTimeout(total=args.timeout)

    locations = args.locations or DEFAULT_LOCATIONS

    async with aiohttp.ClientSession(timeout=timeout) as session:
        tasks = []

        for i in range(args.requests):
            path = random.choice(locations)
            url = f"http://localhost:{args.port}{path}"
            tasks.append(fetch(session, url, sem, i + 1))

        await asyncio.gather(*tasks)


def main():
    parser = argparse.ArgumentParser(description="Async HTTP load generator")

    parser.add_argument(
        "-n", "--requests",
        type=int,
        required=True,
        help="Total number of requests"
    )
    parser.add_argument(
        "-c", "--concurrency",
        type=int,
        default=10,
        help="Concurrent requests"
    )
    parser.add_argument(
        "-p", "--port",
        type=int,
        default=80,
        help="Target port"
    )
    parser.add_argument(
        "-t", "--timeout",
        type=int,
        default=5,
        help="Request timeout"
    )
    parser.add_argument(
        "-l", "--locations",
        type=parse_locations,
        help='JSON array of locations, e.g. \'["/", "/health"]\''
    )

    args = parser.parse_args()
    asyncio.run(run(args))


if __name__ == "__main__":
    main()