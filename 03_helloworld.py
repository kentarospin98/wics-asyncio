import asyncio

async def task(some_value):
    print(some_value)

async def main():
    await task("Hello I'm Task 1")
    await task("Hi I'm Task 2")

asyncio.run(main())

