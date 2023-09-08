import asyncio

async def main():
    print("Hello World")

main_coroutine = main()
print("What is this:", main_coroutine)

asyncio.run(main_coroutine)