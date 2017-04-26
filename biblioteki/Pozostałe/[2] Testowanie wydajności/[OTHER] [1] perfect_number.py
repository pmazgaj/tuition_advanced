def dividers(number):
    """
    :param number: integer, number to get all equal dividers from
    :return: Return list of every integer divide
    """

    return [x for x in range(1, number) if number % x == 0]


def is_perfect_number(number):
    """
    :param number: integer, number to check if it is perfect one (equals sum of all its dividers)
    :return: Checks whether number is perfect or not
    """
    return True if sum(dividers(number)) == number else False


assert is_perfect_number(6) == True, "Valid example"
assert is_perfect_number(5) == False, "Valid example"


def get_perfect_numbers_in_range(x_min=0, x_max=100):
    """
    :param x_min: starting x in range to be set
    :param x_max: ending x in range to be set
    :return: Return list of perfect numbers in given range (x_max + 1 - range doesn't take last argument)
    """

    return [x for x in range(x_min, x_max + 1) if is_perfect_number]


def print_value(value_label=""):
    """
    :param value_label: value to be shown in formatted string
    Prints formatted value """
    print("Setting value for {}".format(value_label))


def set_value(value_label="") -> int:
    """
    :param value_label: starting/ending x in range to be set
    :return: Set (int)value for a range
    """
    value = input("Gimme value for range\n")
    try:
        while not str.isdigit(value):
            value = input("Gimme value for range\n")
        else:
            print_value(value_label)
            value = int(value)
    except TypeError:
        pass
    finally:

        return value


assert isinstance(get_perfect_numbers_in_range(x_min=set_value(value_label="min"), x_max=set_value(value_label="max")),
                  list), "Perfect numbers  - only one"
