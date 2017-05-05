"""
Nodule for asynchronously saving files and computing data
"""
import os
import asyncio
import sys

__author__ = "Przemek"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(BASE_DIR)
FILES_DIR = os.path.dirname(os.path.join(BASE_DIR, 'async', ''))


def create_directory(directory):
    """Create directory for files, if not exist"""
    base_dir = BASE_DIR
    if not os.path.exists(directory):
        os.makedirs(directory)
    return os.path.dirname(os.path.abspath(directory)) + '\{}'.format(directory)

async def compute_values(x, y, z):
    return (x * y) / z


async def save_values(x, y, z, path, name):
    while True:
        await compute_values(x, y, z)
        with open(path + '\{}.txt'.format(name), mode='w+') as file:
            file.write(compute_values(x, y ))


def got_result(future):
    print(future.result())


files_dir = create_directory('filess')
# main event loop
loop = asyncio.get_event_loop()

# Create a task from coroutine
task = loop.create_task(save_values(2, 4, 6, files_dir, 'log'))

# Please notify when task is completed
task.add_done_callback(got_result)

# The loop will run forever
loop.run_until_complete(task)
