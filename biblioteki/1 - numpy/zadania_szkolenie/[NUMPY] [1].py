"""
ZADANIE:
Narysuj wykres funkcji kwadratowej, przedział <-100, 100> (najlepiej zadany)
Pobierz od użytkownika przedział, w którym ma zostać narysowana funkcja.
Stwórz funkcję, formatującą, zwracającą postać f(x): ax^2 + bx + c

Wyrysuj legendę na ekranie.

"""

import matplotlib.pyplot as plt


def create_function_string(a: float, b: float, c: float) -> str:
    """Create the string for function"""
    return "f(x): {}x^2 + {}x + {}".format(a, b, c)


def input_params() -> float:
    """Return valid float number"""
    a = None
    while a is None:
        try:
            a = float(input("Enter a number: \n"))
        except ValueError:
            print("Not an float value...")
    return a


def get_function_value(x_range: range, a: float, b: float, c: float) -> list:
    """Return list og values for function in given range"""

    return [a * (x ** 2) + b * x + c for x in x_range]


def create_basic_curve(x_min: int, x_max: int) -> None:
    """Create curve, show x_min, and x_max"""
    a = input_params()
    b = input_params()
    c = input_params()

    x = range(x_min, x_max)
    y = get_function_value(x, a, b, c)
    function_string = create_function_string(a, b, c)

    plt.plot(x, y, label=function_string)
    plt.legend(loc='best')

    plt.show()


create_basic_curve(-100, 100)
