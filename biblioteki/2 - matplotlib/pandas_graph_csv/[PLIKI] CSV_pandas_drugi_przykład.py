from matplotlib import style
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


link = 'C:/Users/Paweł Rak/PycharmProjects/Szkolenie z Pythona/assets/test_liczby.csv'
PATH = os.path.dirname(os.path.abspath(__file__))

print(PATH)


def make_an_array_from_csv_file():
    """Add every single element to an array..."""
    v1, v2, v3, v4, v5, v6, v7, v8, v9 = np.loadtxt(link, unpack=True, delimiter=',')
    # ładujemy do tablic nazwanych pliki
    return v1, v2, v3



# df = pd.DataFrame(v1, columns=['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])


def draw_chart(what_to_show):
    style.use('ggplot')
    pd.options.display.max_columns = 60
    pd.options.display.max_rows = 6
    plt.plot(range(0, len(what_to_show)), np.float64(what_to_show))
    # plt.plot(np.float64(v1), np.float64(v1))
    plt.title('Sportowe świry')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.grid(False)
    plt.show()


draw_chart(make_an_array_from_csv_file())
