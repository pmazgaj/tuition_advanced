"""
PREZENTACJA:
Stwórzmy podstawowy wykres, na podstawie którego wyświetlimy wynik funkcji na ekran
"""

# importujemy z biblioteki matplotlib wykres..
import matplotlib.pyplot as plt


def create_basic_curve():
    """Tworzymy zwykłą krzywą, oś x -  x, y - wartość"""
    x = range(0, 100)
    y = [value ** 2 for value in x]
    print(y)
    plt.plot(x, y)
    plt.show()

create_basic_curve()
