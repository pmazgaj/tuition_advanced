def argument_test_natural_number(f):
    """ Check, if given number is an integer, and then decorate with it, for factorial operation """

    def helper(x):
        if isinstance(x, int) and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")

    return helper


@argument_test_natural_number
def factorial(n):
    """ Calculate factorial for given number """
    return 1 if n == 1 else n * factorial(n - 1)


for i in range(1, 10):
    # print(i, factorial(i))
    pass


# print(factorial(-1))

def call_counter(func):
    """
    The following example uses a decorator to count the number of times a function has been called.
    To be precise, we can use this decorator solely for functions with exactly one parameter:
    """

    def helper(x):
        helper.calls += 1
        return func(x)

    helper.calls = 0

    return helper


@call_counter
def succ(x):
    return x + 1


print(succ.calls)
for i in range(10):
    succ(i)
    pass
print("Calls of function {}: {}".format(succ.__name__, succ.calls))
