"""
Decorator - logging functionality
"""

import time


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        print(args.__class__)
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        print(args.__class__)
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_info(name, age, wait_time=1):
    # wait wait_time seconds, till showing message
    time.sleep(wait_time)
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info = my_timer(display_info)

# shows wrapper, instead orig
# print(display_info.__name__)

display_info('Przemek', 25)
display_info('Przemek', 44)
display_info('Przemek', 42)
