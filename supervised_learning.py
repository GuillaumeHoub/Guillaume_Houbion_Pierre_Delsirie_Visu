import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

dtypes = {"Id": "int", "Car": "str", "MPG": "float", "Cylinders": "int", "Displacement": "float", "Horsepower": "float", "Weight": "float", "Acceleration": "float", "Model": "int", "Origin": "str"}

df = pd.DataFrame(pd.read_csv("./cars.csv", header=0, dtype=dtypes))
#df = df.loc[:, ["Weight", "MPG"]]
x = df.loc[:, "Weight"].values.reshape((-1, 1))
y = df.loc[:, "MPG"].values
model = LinearRegression()
model.fit(x, y)
print("coefficient de determination : ", model.score(x, y))
poids = [[4000.0]]
print("Prédiction du MPG pour un poid de ", poids[0][0], " est : ", model.predict([[4000.0]])[0])
