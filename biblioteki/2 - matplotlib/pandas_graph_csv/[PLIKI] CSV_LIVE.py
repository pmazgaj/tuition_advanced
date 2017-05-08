import matplotlib.animation as ani
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

link = 'C:/Users/Paweł Rak/PycharmProjects/Szkolenie z Pythona/assets/test_liczby.csv'
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def get_arrays_from_csv_data(path):
    stock_data = pd.read_csv(link,
                             names=['Imię', 'Nazwisko', 'ID', 'Wiek', 'Wynik testu', 'Wynik w semestrze', "Średni wynik"])

    # dostajemy się do wartości po names (kolumna)
    imie = list(stock_data["Imię"])
    nazwisko = list(stock_data["Nazwisko"])
    identyfikator = list(stock_data["ID"])
    test_wynik = list(stock_data["Wynik testu"])
    semestr_wynik = list(stock_data["Wynik w semestrze"])
    wiek = list(stock_data["Wiek"])

    # srednia_ocen = list(stock_data["Średni wynik"]) == [x/5 for x in range(0, len(semestr_wynik))]
    # print(srednia_ocen)

    print(stock_data)
    return imie


def draw_chart(what_to_show):
    print(what_to_show)
    pd.options.display.max_columns = 60
    pd.options.display.max_rows = 6

    x = range(0, len(what_to_show))
    y = what_to_show

    ax1.plot(x, y)

    # linia z przeciętnym wynikiem
    plt.axhline(sum(y) / len(what_to_show))
    return what_to_show


def animate(i):
    draw_chart(get_arrays_from_csv_data(link))

an = ani.FuncAnimation(fig, animate, interval=1000)
plt.show()

