import asyncio
from concurrent.futures import ThreadPoolExecutor
import quandl

# Initialize 10 threads
tp = ThreadPoolExecutor(10)


def handler(code, future):
    exc = None

    try:
        print("Start downloading.")
        dataset = quandl.Dataset(code)
        print(dataset)
        print("Downloading finished.")
    except Exception as _exc:
        exc = _exc

    if exc is None:
        def clb():
            future.set_result(dataset)
    else:
        def clb():
            future.set_exception(exc)

    loop = asyncio.get_event_loop()
    loop.call_soon_threadsafe(clb)


def wrapper(code):
    future = asyncio.Future()
    tp.submit(handler, code, future)

    return future


# somewhere else
async def main():
    result1 = await wrapper("SIX/US9884981013EUR4")
    print("ABC")
    # result2 = await wrapper("SIX/US88160R1014EUR4")

    print(result1)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
