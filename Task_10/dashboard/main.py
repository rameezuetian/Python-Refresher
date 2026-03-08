import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


async def fetch_source1():
    await asyncio.sleep(1)
    return {"sales": 100}


async def fetch_source2():
    await asyncio.sleep(2)
    return {"sales": 200}


async def fetch_source3():
    await asyncio.sleep(1.5)
    return {"sales": 150}


async def collect_data():

    results = await asyncio.gather(
        fetch_source1(),
        fetch_source2(),
        fetch_source3()
    )

    return results


def merge_data(data):

    total_sales = sum(d["sales"] for d in data)

    return {
        "sources": len(data),
        "total_sales": total_sales
    }


async def main():

    data = await collect_data()

    summary = merge_data(data)

    print("Dashboard Summary")
    print(summary)


asyncio.run(main())