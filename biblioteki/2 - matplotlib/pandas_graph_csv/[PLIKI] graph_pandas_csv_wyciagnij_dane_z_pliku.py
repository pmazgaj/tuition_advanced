"""
ZADANIE:
Mamy dany plik .csv. Wyświetlmy na ekran jego zawartość, tworząc listy, przy użyciu biblioteki pandas i modułu read_csv.
Wypisz średnią wartość dla kolumny wynik punktowy (ostatnia utworzona kolumna, powinna dostać taką nazwę)
Sprawdź, jaki średni wynik zalicza użytkownik (zakładając, że do tej pory odbyło się 5 testów, punktowanych po 100 pkt.)
Zwróć to, w postaci listy ze średnimi dla użytkowników.
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
"""
axvline – A full vertical line (does not start or stop)
vlines – A vertical line segment (or multiple)
axhline – A full horizontal line
hlines – …
"""
FULL_PATH = os.path.realpath(__file__)
DIRECTORY_PATH = os.path.dirname(os.getcwd())

ASSETS_PATH = os.path.dirname(os.path.join(DIRECTORY_PATH, 'tuition_advanced', 'biblioteki',
                                           '2 - matplotlib', 'assets'))

print(DIRECTORY_PATH)
print(FULL_PATH)
print(ASSETS_PATH)


def get_mean(list_to_get_mean):
    """return an average value for list (based on numpy)"""
    return np.mean(list_to_get_mean)


def get_arrays_from_csv_data(path):
    stock_data = pd.read_csv(PATH,
                             names=['Imię', 'Nazwisko', 'ID', 'Wiek', 'Wynik testu', 'Wynik w semestrze',
                                    "Średni wynik"])

    # dostajemy się do wartości po names (kolumna)
    name = list(stock_data["Imię"])
    last_name = list(stock_data["Nazwisko"])
    identifier = list(stock_data["ID"])
    test_result = list(stock_data["Wynik testu"])
    semestr_result = list(stock_data["Wynik w semestrze"])
    age = list(stock_data["Wiek"])

    print(stock_data)
    return test_result


def draw_chart(what_to_show):
    pd.options.display.max_columns = 60
    pd.options.display.max_rows = 6
    x = range(0, len(what_to_show))
    y = what_to_show

    plt.plot(x, y)

    # linia z przeciętnym wynikiem
    plt.axhline(sum(y) / len(what_to_show))
    plt.show()


# draw_chart(get_arrays_from_csv_data(PATH))
