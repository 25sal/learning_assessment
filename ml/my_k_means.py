from sklearn.cluster import KMeans
import numpy as np
from models.enums import ErrorTopics, Grades
from utils.plotHelper import plot_k_means_based_on_features


def my_k_means(data):
    data_array = np.array(data)
    num_clusters = 6
    kmeans = KMeans(num_clusters, random_state=42)
    # Get cluster assignments for each data point
    cluster_labels = kmeans.fit_predict(data_array)
    print(cluster_labels)

    # Print cluster assignments
    # for i, cluster in enumerate(cluster_labels):
    #     print(f"Data point {i + 1} belongs to cluster {cluster}")
    plot(data_array, cluster_labels)


def plot(data_array, cluster_labels):
    print('Plots:')

    # plot_based_on_features_with_multiplicity(data_array, cluster_labels, ErrorTopics.assignment, ErrorTopics.initialization)
    
    plot_k_means_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.conflict, True)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.incompatibility)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.assignment)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.initialization)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.parameters)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declaration, ErrorTopics.array)

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.conflict, ErrorTopics.incompatibility)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.conflict, ErrorTopics.assignment)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.conflict, ErrorTopics.initialization)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.conflict, ErrorTopics.parameters)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.conflict, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.conflict, ErrorTopics.array)

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.incompatibility, ErrorTopics.assignment)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.incompatibility, ErrorTopics.initialization)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.incompatibility, ErrorTopics.parameters)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.incompatibility, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.incompatibility, ErrorTopics.array)

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.assignment, ErrorTopics.initialization)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.assignment, ErrorTopics.parameters)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.assignment, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.assignment, ErrorTopics.array)

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.initialization, ErrorTopics.parameters)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.initialization, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.initialization, ErrorTopics.array)

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.parameters, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.parameters, ErrorTopics.array)

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.syntax, ErrorTopics.array)

