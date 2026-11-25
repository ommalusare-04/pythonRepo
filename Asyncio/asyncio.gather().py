import asyncio

async def student1():
    print("student 1 started studying")
    await asyncio.sleep(4)
    print("student 1 completed studying")

async def student2():
    print("student 2 started studying")
    await asyncio.sleep(2)
    print("student 2 completed studying")

async def main():
    await asyncio.gather(student1(),student2())

asyncio.run(main())