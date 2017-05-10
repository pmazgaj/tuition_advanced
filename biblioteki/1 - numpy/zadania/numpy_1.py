"""
PREZENTACJA:
Stwórzmy podstawowy wykres, na podstawie którego wyświetlimy wynik funkcji na ekran
"""

# importujemy z biblioteki matplotlib wykres..
from matplotlib import pyplot as plt


def create_basic_curve():
    """Tworzymy zwykłą krzywą, oś x -  x, y - wartość"""
    x_range = range(0, 100)
    y_range = [value ** 2 for value in x_range]
    print(y_range)
    plt.plot(x_range, y_range)
    plt.show()


create_basic_curve()
