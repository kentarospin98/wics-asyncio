import asyncio

async def task(some_value):
    print(some_value)

async def main():
    task_1_coro = task("Hello I'm Task 1")
    task_2_coro = task("Hi I'm Task 2")

    await task_1_coro
    await task_2_coro

main_coroutine = main()
asyncio.run(main_coroutine)

