import asyncio

async def hello():
    r = ''
    print("Hello world!")
    # 异步调用asyncio.sleep(1):

    r = await range1(5)
    print("%s"%r)
    print("Hello again!")
async def range1(x):
   # await asyncio.sleep(1)
    return "ddd"


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()