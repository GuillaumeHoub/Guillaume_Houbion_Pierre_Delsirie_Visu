from visualization_1 import get_interval
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt


dtypes = {"Id": "int", "Car": "str", "MPG": "float", "Cylinders": "int", "Displacement": "float", "Horsepower": "float",
          "Weight": "float", "Acceleration": "float", "Model": "int", "Origin": "str"}

df = pd.DataFrame(pd.read_csv("./cars.csv", header=0, dtype=dtypes))


def visualize(interval, columns):
    data = df.loc[intervalle[0]:intervalle[1], [columns[0], columns[1]]]
    values = data.values
    sns.scatterplot(x=values[:, 0], y=values[:, 1])
    plt.xlabel(columns[0])
    plt.ylabel(columns[1])
    plt.title("Scatterplot")
    plt.savefig("scatter_plot_cars.pdf")
    plt.show()
    plt.close()

def get_column():
    pattern = re.compile('^[A-z]+-[A-z]+$')
    print("Entrez les deux colonnes que vous souhaitez afficher sur le scatterplot")
    print("Colonnes disponibles: MPG (Miles per gallon), Acceleration, Cylinders, Displacement, Horsepower, Weight")
    print("Entrez les deux colonnes séparé par un tiret (Exemple: Weight-MPG ou Cylinders-Acceleration)")
    while 1:
        intervalle = input("Colonnes : ")
        if intervalle == "":
            return ["Acceleration", "Weight"]
        match = re.search(pattern, intervalle)
        if match:
            columns = intervalle.split("-")
            if columns[0] in df and columns[1] in df:
                return [columns[0], columns[1]]
            else:
                print("Mauvaises colonnes")


if __name__ == '__main__':
    intervalle = get_interval()
    colonnes = get_column()
    visualize(intervalle, colonnes)
