from sklearn.cluster import KMeans
import numpy as np
from models.enums import ErrorType, Grade
from utils.plotHelper import plot_k_means_based_on_features
import matplotlib.pyplot as plt


def my_k_means(data, nclusters):
    data_array = np.array(data)
    print(len(data_array))
    num_clusters = nclusters
    kmeans = KMeans(num_clusters, random_state=42)
    # Get cluster assignments for each data point
    cluster_labels = kmeans.fit_predict(data_array)
    total_cluster = np.zeros(num_clusters)
    for i in range(len(cluster_labels)):
        total_cluster[cluster_labels[i]] +=data_array[i].sum() 
    print(total_cluster)

    # Count the number of points in each cluster
    cluster_counts = np.bincount(cluster_labels)

    # Print the number of points in each cluster

    for i, count in enumerate(cluster_counts):
        percentage = (count / len(data_array)) * 100
        print(f"Cluster {i+1}: {count} points, " + f"percentuale: {percentage}")
    # ! If I print and copy the centroids matrix it works, if I pass the centroids from kmeans it does not
    centroids = kmeans.cluster_centers_
    return(centroids)
    # plot(data_array, cluster_labels)


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