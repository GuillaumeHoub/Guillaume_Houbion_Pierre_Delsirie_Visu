import numpy as np

def generate_artificial_dataset():
    num_samples = 300

    mu = np.array([2.5, 4.0, 10.0])

    r = np.array([
        [3.40, -2.75, -3.20],
        [-2.75, 5.50, 4.50],
        [-3.20, 4.50, 4.25],
    ])

    r2 = np.array([
        [1, 0],
        [0, 2],
    ])

    rng = np.random.default_rng()
    y = rng.multivariate_normal(mu, r, size=num_samples)
    y2 = rng.multivariate_normal([1, -1], r2, size=num_samples)
    #print(np.corrcoef(y, rowvar=False))
    #print(np.corrcoef(y2, rowvar=False))
    data = np.concatenate((y, y2), axis=1)
    int_array = np.random.randint(100, size=(300, 1))
    data = np.concatenate((data, int_array), axis=1)
    print("Matrice de corrélation :")
    print("-----------------------------")
    print(np.corrcoef(data, rowvar=False), "\n")
    print("Moyennes des colonnes :")
    print("-----------------------------")
    print(data.mean(0), "\n")
    print("Ecart type des colonnes :")
    print("-----------------------------")
    print(data.std(0))
    np.save("artificial_dataset", data)


if __name__ == '__main__':
    generate_artificial_dataset()