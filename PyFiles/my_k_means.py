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


def my_k_means(data):

    data_array = np.array(data)
    # Applico il kMeans utilizzando 10 come numero di cluster
    kmeans = KMeans(n_clusters=10)  # 6 !!!
    kmeans.fit(data_array)
    predictions = kmeans.predict(data_array)
    # Get cluster assignments for each data point
    cluster_assignments = kmeans.labels_

    # Print cluster assignments
    for i, cluster in enumerate(cluster_assignments):
        print(f"Data point {i + 1} belongs to cluster {cluster}")



