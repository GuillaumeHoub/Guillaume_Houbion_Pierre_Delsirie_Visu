from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dtypes = {"Id": "int", "Car": "str", "MPG": "float", "Cylinders": "int", "Displacement": "float", "Horsepower": "float",
          "Weight": "float", "Acceleration": "float", "Model": "int", "Origin": "str"}

df = pd.DataFrame(pd.read_csv("./cars.csv", header=0, dtype=dtypes))
df = df.loc[:, ["Acceleration", "Weight", "Cylinders", "Displacement", "Horsepower", "MPG"]]
data = df.values


def elbow_method():
    inertia = []
    K = range(1, 11)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(data)
        inertia.append(km.inertia_)
    sns.lineplot(x=range(1, 11), y=inertia, marker='o')
    plt.xlabel('k')
    plt.ylabel('Inertia')
    plt.title('Elbow Method For Optimal k')
    plt.show()


def apply_clustering(k):
    kmeans = KMeans(n_clusters=3, random_state=100)
    kmeans.fit(data[:, [0, 1]])
    clusters = kmeans.predict(data[:, [0, 1]])
    centers = np.array(kmeans.cluster_centers_)
    sns.scatterplot(x=data[:, 0], y=data[:, 1], hue=clusters)
    sns.scatterplot(x=centers[:, 0], y=centers[:, 1], s=100, color='y')
    plt.xlabel('Acceleration')
    plt.ylabel('Weight')
    plt.show()
    kmeans.fit(data[:, [4, 5]])
    clusters = kmeans.predict(data[:, [4, 5]])
    centers = np.array(kmeans.cluster_centers_)
    sns.scatterplot(x=data[:, 4], y=data[:, 5], hue=clusters)
    sns.scatterplot(x=centers[:, 0], y=centers[:, 1], s=100, color='y', label="Centers")
    plt.xlabel('Horsepower')
    plt.ylabel('MPG (Miles per Gallon)')
    plt.show()


if __name__ == '__main__':
    elbow_method()
    apply_clustering(3)
