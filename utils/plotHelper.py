import numpy as np
import matplotlib.pyplot as plt
from models.DevelopmentProcess import DevelopmentProcess
from models.DevelopmentSession import DevelopmentSession
from models.enums import ErrorTopics
from collections import defaultdict


def plot_k_means_based_on_features(data_array, cluster_labels,
                                   feature_1=ErrorTopics.declaration,
                                   feature_2=ErrorTopics.array,
                                   print_multiplicity=False,
                                   num_clusters=6
                                   ):
    plt.figure(figsize=(8, 6))

    # Create a scatter plot for each cluster
    for cluster_idx in range(num_clusters):
        cluster_points = data_array[cluster_labels == cluster_idx]

        plt.scatter(cluster_points[:, feature_1.value],
                    cluster_points[:, feature_2.value],
                    label=f'Cluster: {cluster_idx + 1}')

    if print_multiplicity:
        coord_counts = defaultdict(int)
        for coord, label in zip(data_array, cluster_labels):
            coord = [coord[feature_1.value], coord[feature_2.value]]
            coord_str = tuple(coord)
            coord_counts[coord_str] += 1

        for coord, count in coord_counts.items():
            plt.annotate(count, coord, textcoords="offset points", xytext=(0, -3), ha='center', fontsize=7)
            
    plt.title('Cluster Visualization')
    plt.xlabel(str(feature_1))
    plt.ylabel(str(feature_2))
    plt.legend()
    plt.show()


def plot_student_progression(ds_array, feature_1=ErrorTopics.declaration, feature_2=ErrorTopics.array):
    errors = []
    exam_ids = []
    for ds in ds_array:
        exam_ids.append(ds.exam_id)
        errors.append(ds.errors)

    errors = np.array(errors)
    n_exams = list(range(len(exam_ids)))

    # Create a line plot
    plt.figure(figsize=(8, 6))
    plt.plot(n_exams, errors[:, feature_1.value], label=str(feature_1), marker='o', linestyle='-')
    plt.plot(n_exams, errors[:, feature_2.value], label=str(feature_2), marker='s', linestyle='--')
    plt.xticks(list(map(int, n_exams)))
    plt.xlabel('Exam IDs')
    plt.ylabel('Value')
    plt.title('Change of ' + str(feature_1) + ' and ' + str(feature_2))
    plt.legend()
    # plt.grid(True)
    plt.show()


def plot_normalized_errors_and_lines(developer_sessions, feature=ErrorTopics.declaration):
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    for i in range(len(developer_sessions)):
        plt.bar(developer_sessions[i].lines, developer_sessions[i].normalized_errors[feature.value])

    plt.xlabel("lines")
    plt.ylabel("number of normalized" + str(feature))
    plt.savefig("/Users/leobartowski/Documents/Tesi/Plots/ErrorsAndLines/Normalized/" + str(feature) + '.png', dpi=300, bbox_inches="tight")
    # plt.show()


def plot_errors_and_lines(developer_sessions, feature=ErrorTopics.declaration):
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    for i in range(len(developer_sessions)):
        plt.bar(developer_sessions[i].lines, developer_sessions[i].errors[feature.value])

    plt.xlabel("lines")
    plt.ylabel("number of " + str(feature))

    plt.savefig("/Users/leobartowski/Documents/Tesi/Plots/ErrorsAndLines/NotNormalized/" + str(feature) + '.png', dpi=300, bbox_inches="tight")
    # plt.show()




