import asyncio
async def greet():
    print("hello")
    await asyncio.sleep(4)
    print("Welcome to Asyncio")
asyncio.run(greet()) 