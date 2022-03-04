import re
import plotly.express as px
import pandas as pd

dtypes = {"Id": "int", "Car": "str", "MPG": "float", "Cylinders": "int", "Displacement": "float", "Horsepower": "float", "Weight": "float", "Acceleration": "float", "Model": "int", "Origin": "str"}

df = pd.DataFrame(pd.read_csv("./cars.csv", header=0, dtype=dtypes))
df = df.loc[:, ["Acceleration", "Weight", "Cylinders", "Displacement", "Horsepower", "MPG"]]

def visualize(intervalle):
    labels = {"MPG": "MPG", "Cylinders": "Cylinders", "Displacement": "Displacement", "Horsepower": "Horsepower", "Weight": "Weight", "Acceleration": "Acceleration"}
    data = df.loc[intervalle[0]:intervalle[1], :]
    fig = px.parallel_coordinates(data,
                                  color="MPG",
                                  labels=labels,
                                  color_continuous_scale=px.colors.diverging.RdYlBu,
    )
    fig.show()


def get_interval():
    pattern = re.compile('^[0-9]+-[0-9]+$')
    print("Entrez l'intervalle de point que vous souhaitez visualiser (laisser vide pour garder les valeurs par défaut)")
    print("Entrez les deux valeurs de l'intervalle séparé par un tiret (Exemple: 0-50 ou 100-200)")
    while 1:
        intervalle = input("Intervalle : ")
        if intervalle == "":
            return [0, 390]
        match = re.search(pattern, intervalle)
        if match:
            inter = intervalle.split("-")
            beginning = int(inter[0])
            end = int(inter[1])
            if beginning < 0 or end > 390 or beginning >= end:
                print("Error !")
            else:
                return [beginning, end]
        print("Mauvais Intervalle")


if __name__ == '__main__':
    intervalle = get_interval()
    visualize(intervalle)

