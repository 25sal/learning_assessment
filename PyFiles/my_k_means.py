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

    plot_based_on_features(data_array, cluster_labels, ErrorTopics.declarations, ErrorTopics.array)


def plot_based_on_features(data_array, cluster_labels,
                           feature_1=ErrorTopics.declarations,
                           feature_2=ErrorTopics.array,
                           num_clusters=6, ):
    plt.figure(figsize=(8, 6))

    # Create a scatter plot for each cluster
    for cluster_idx in range(num_clusters):
        cluster_points = data_array[cluster_labels == cluster_idx]

        plt.scatter(cluster_points[:, ErrorTopics.declarations.value],
                    cluster_points[:, ErrorTopics.array.value],
                    label=f'Cluster: {Grades(cluster_idx + 1).name}')

    plt.title('Cluster Visualization')
    plt.xlabel(str(feature_1))
    plt.ylabel(str(feature_2))
    plt.legend()
    plt.show()
