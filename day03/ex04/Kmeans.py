import numpy as np
import pandas as pd
import random as rd
from matplotlib import pyplot as plt


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroides = []

    def fit(self, X):
        self.centroides = np.array([]).reshape(3, 0)
        for i in range(self.ncentroid):
            rand = rd.randint(0, len(X) - 1)
            self.centroides = np.c_[self.centroides, X[rand]]
        output = {}
        for i in range(self.max_iter):
            euclidian_dist = np.array([]).reshape(len(X), 0)
            # for take distance between data and all centroids and 90º rot
            for k in range(self.ncentroid):
                tmp = np.sum((X - self.centroides[:, k]) ** 2, axis=1)
                euclidian_dist = np.c_[euclidian_dist, tmp]
            # find minimum dist and store it
            min_dist_index = np.argmin(euclidian_dist, axis=1) + 1
            dtmp = {}
            # init the tmp array
            for k in range(self.ncentroid):
                dtmp[k + 1] = np.array([]).reshape(3, 0)
            # regroup the data points based of the index of the min distances
            for i in range(len(X)):
                dtmp[min_dist_index[i]] = np.c_[dtmp[min_dist_index[i]], X[i]]
            # do transpose for each centroide
            for k in range(self.ncentroid):
                dtmp[k + 1] = dtmp[k + 1].T
            # compute the mean of separated clusters and assign it as new
            # centroides
            plt.figure()
            for k in range(self.ncentroid):
                self.centroides[:, k] = np.mean(dtmp[k + 1], axis=0)
            output = dtmp
            color = ['red', 'blue', 'green', 'cyan', 'magenta']
            labels = ['cluster1', 'cluster2', 'cluster3', 'cluster4',
                      'cluster5']
            for k in range(self.ncentroid):
                plt.scatter(output[k + 1][:, 0], output[k + 1][:, 1],
                            c=color[k], label=labels[k])
            plt.scatter(self.centroides[0, :], self.centroides[1, :], s=300,
                        c='yellow', label='Centroids')
            plt.show()

    def predict(self, X):
        dist = float("inf")
        for k in range(self.ncentroid):
            tmp = sum((X - self.centroides[:, k]) ** 2)
            if tmp < dist:
                dist = tmp
        return dist


dataset = pd.read_csv('system_census.csv')
dataset.describe()

X = dataset.iloc[:, [1, 2, 3]].values

Kmeans = KmeansClustering()

Kmeans.fit(X)

Kmeans.predict(X[0])
