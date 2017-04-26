def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result


# print(temperature(20))


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")


def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__)


# f(g)

import math


def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res


# print(foo(math.sin))
# print(foo(math.cos))


def f(x):
    def g(y):
        return y + x + 3

    return g


# kolejność wywołania - argumenty zewnętrznej funkcji, potem wewnętrznej
# nf1 = f(1)(1)
# nf2 = f(3)(1)

# print(nf1)
# print(nf2)

# nf1 = f(1)
# nf2 = f(3)

# print(nf1)
# print(nf2)

def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x ** 2 + b * x + c

    return polynomial


p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    # print(x, p1(x), p2(x))
    pass


def polynomial_creator(*coefficients):
    def polynomial(x):
        res = 0
        degree = len(coefficients) - 1
        for index, coeff in enumerate(coefficients):
            res += coeff * x ** (degree - index)
        return res

    return polynomial


# p1 = polynomial_creator(4)
# p2 = polynomial_creator(2, 4)
# p3 = polynomial_creator(2, 3, -1, 8, 1)
# p4 = polynomial_creator(-1, 2, 1)
#
# for x in range(-2, 2, 1):
#     print(x, p1(x), p2(x), p3(x), p4(x))


def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)

    return function_wrapper


@our_decorator
def succ(n):
    return n + 1


succ(10)
