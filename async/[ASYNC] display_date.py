import asyncio
import datetime
import random


@asyncio.coroutine
def display_date(num, loop_to_run):
    """display date for loop, created for specific event"""
    end_time = loop_to_run.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop_to_run.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))


async def display_date_2(num, loop_to_run, ):
    """display date for loop, created for specific event"""
    end_time = loop_to_run.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop_to_run.time() + 1.0) >= end_time:
            break
        """Function is paused, until yield statement gets a value"""
        await asyncio.sleep(random.randint(0, 5))


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date_2(2, loop))

loop.run_forever()
