import asyncio

async def main():
    task = asyncio.create_task(func1()) 
    print('main1')
    await asyncio.sleep(5)
    print('main2')
    ret_val = await task
    print(f"Return value was {ret_val}")

async def func1():
    print('A')
    await asyncio.sleep(2)
    print('B')
    return 10

asyncio.run(main())