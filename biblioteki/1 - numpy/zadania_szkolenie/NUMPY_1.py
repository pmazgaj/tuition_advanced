"""
ZADANIE:
Narysuj wykres funkcji kwadratowej, przedział <-100, 100> (najlepiej zadany)
Pobierz od użytkownika przedział, w którym ma zostać narysowana funkcja.
Stwórz funkcję, formatującą, zwracającą postać f(x): ax^2 + bx + c

Wyrysuj legendę na ekranie.

"""

from matplotlib import pyplot as plt


def create_function_string(coefficient_a: float, coefficient_b: float, coefficient_c: float) -> str:
    """
    Create the string for function
    :param coefficient_a:
    :param coefficient_b:
    :param coefficient_c:
    :return:
    """
    return "f(x): {}x^2 + {}x + {}".format(coefficient_a, coefficient_b, coefficient_c)


def input_params() -> float:
    """
    Return
    :return: valid float number
    """
    # set number - None
    number = None
    while number is None:
        try:
            number = float(input("Enter a number: \n"))
        except ValueError:
            print("Not an float value...")
    return number


def get_function_value(x_range: range, coefficient_a: float,
                       coefficient_b: float, coefficient_c: float) -> list:
    """
    Return list of values for function in given range"
    :param x_range:
    :param coefficient_a:
    :param coefficient_b:
    :param coefficient_c:
    :return:
    """
    return [coefficient_a * (x ** 2) + coefficient_b * x + coefficient_c for x in x_range]


def create_basic_curve(x_min: int, x_max: int) -> None:
    """
    Create curve, show x_min, and x_max
    :param x_min:
    :param x_max:
    :return:
    """
    # set coefficients for function, from user

    coefficient_a = input_params()
    coefficient_b = input_params()
    coefficient_c = input_params()

    x_range = range(x_min, x_max)
    y_range = get_function_value(x_range, coefficient_a, coefficient_b, coefficient_c)
    function_string = create_function_string(coefficient_a, coefficient_b, coefficient_c)

    plt.plot(x_range, y_range, label=function_string)
    plt.legend(loc='best')

    plt.show()


create_basic_curve(-100, 100)
