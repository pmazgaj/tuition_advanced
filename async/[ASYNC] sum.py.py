import asyncio
import random


async def compute(x, y):
    print("Compute {} + {} ...".format(x, y))
    # wait 1.0 second till returning value
    await asyncio.sleep(1.0)
    return x + y


async def print_sum():
    result = await compute(random.randint(0, 100), random.randint(0, 100))
    await save_to_file(result)
    result = await compute(random.randint(0, 100), random.randint(0, 100))
    await save_to_file(result)

    print("result = {}".format(result))


async def save_to_file(result):
    with open('plik_async.txt', 'a+') as file:
        file.write('{}'.format(result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum())
loop.close()
