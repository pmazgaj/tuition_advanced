from timeit import timeit


# print(timeit("list()"))
# print(timeit("tuple()"))
# print(timeit("()"))
# print(timeit("[]"))
# print(timeit("dict()"))
# print(timeit("{}"))
# print(timeit("dict"))
# print(timeit("set()"))


def first_list_performance() -> str:
    return str([x ** 3 for x in range(0, 100)])


def second_list_performance():
    x_list = []
    for x in range(0, 100):
        x_list.append(x ** 3)
    return str(x_list)


def third_list_performance():
    x_list = []
    x = 0
    while x < 100:
        x_list.append(x ** 3)
        x += 1
    return str(x_list)


def get_yield_num_range(number):
    while True:
        if number < 100:
            number = yield number
        number += 1


def print_successive_primes(iterations=2):
    prime_generator = get_yield_num_range(iterations)
    prime_generator.send(None)
    for power in range(iterations):
        print(prime_generator.send(iterations ** power))


# print("List comprehension: {}".format(timeit(first_list_performance())))
# print("For loop: {}".format(timeit(second_list_performance())))
# print("While loop: {}".format(timeit(third_list_performance())))


yp = print_successive_primes(10)
print(next(yp))
print(next(yp))
print(next(yp))
# print("Yield loop: {}".format(timeit(yield_performance())))
