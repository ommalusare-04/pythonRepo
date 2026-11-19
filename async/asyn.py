import asyncio

async def fn2():
    await asyncio.sleep(3)
    print("four")
    await asyncio.sleep(3)
    print("five")

async def main():
    print("one")
    await asyncio.sleep(2)
    await fn2()
    
    print("two")
    await asyncio.sleep(2)
    await fn2()
    
    print("three")
    await asyncio.sleep(2)
    await fn2()
    

asyncio.run(main())