import asyncio

async def task(some_value):
    await asyncio.sleep(1)
    print(some_value)

async def main():
    await task("Hello I'm Task 1")
    await task("Hi I'm Task 2")

asyncio.run(main())

