import asyncio
import httpx

async def task(some_value):
    await asyncio.sleep(1)
    print(some_value)

async def main():
    task_1_coro = task("Hello I'm Task 1")
    task_2_coro = task("Hi I'm Task 2")

    await asyncio.gather(task_1_coro, task_2_coro)

asyncio.run(main())

