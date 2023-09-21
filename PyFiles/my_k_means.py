from sklearn import datasets, neighbors, linear_model, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.cluster import KMeans
from sklearn import tree
from sklearn.model_selection import GridSearchCV
import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import Image
from sklearn.tree import export_graphviz
from subprocess import call
from sklearn.metrics import silhouette_score
from yellowbrick.cluster import KElbowVisualizer, SilhouetteVisualizer

from data_structures.enums import ErrorTopics, Grades


def my_k_means(data):
    data_array = np.array(data)
    num_clusters = 6
    kmeans = KMeans(num_clusters, random_state=42)
    # Get cluster assignments for each data point
    cluster_labels = kmeans.fit_predict(data_array)

    # Print cluster assignments
    # for i, cluster in enumerate(cluster_labels):
    #     print(f"Data point {i + 1} belongs to cluster {cluster}")

    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.conflict)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.incompatibility)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.assignment)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.initialization)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.parameters)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.syntax)
    # plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.array)

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

