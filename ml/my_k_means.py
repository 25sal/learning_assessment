from sklearn.cluster import KMeans
import numpy as np
from models.enums import ErrorType, Grade
from utils.plotHelper import plot_k_means_based_on_features
import matplotlib.pyplot as plt


def my_k_means(data):
    data_array = np.array(data)
    num_clusters = 6
    kmeans = KMeans(num_clusters, random_state=42)
    # Get cluster assignments for each data point
    cluster_labels = kmeans.fit_predict(data_array)
    # Print cluster assignments
    # for i, cluster in enumerate(cluster_labels):
    #     print(f"Data point {i + 1} belongs to cluster {cluster}")
    # plot(data_array, cluster_labels)
    # ! If I print and copy the centroids matrix it works, if I pass the centroids from kmeans it does not
    centroids = kmeans.cluster_centers_
    # print(centroids)


def plot(data_array, cluster_labels):
    # this double iterate through the category 2 by 2 avoiding replications
    for i in range(8):
        for j in range(i + 1, 8):
            plot_k_means_based_on_features(data_array,
                                           cluster_labels,
                                           "/Users/leobartowski/Documents/Tesi/Plots/kMeans/NotNormalized/",
                                           ErrorType(i),
                                           ErrorType(j),
                                           True,
                                           )