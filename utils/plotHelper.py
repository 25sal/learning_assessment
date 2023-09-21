import numpy as np
import matplotlib.pyplot as plt
from data_structures.DevelopmentProcess import DevelopmentProcess
from data_structures.DevelopmentSession import DevelopmentSession
from data_structures.enums import ErrorTopics


def plot_based_on_features(data_array, cluster_labels,
                           feature_1=ErrorTopics.declarations,
                           feature_2=ErrorTopics.array,
                           num_clusters=6
                           ):
    plt.figure(figsize=(8, 6))

    # Create a scatter plot for each cluster
    for cluster_idx in range(num_clusters):
        cluster_points = data_array[cluster_labels == cluster_idx]

        plt.scatter(cluster_points[:, feature_1.value],
                    cluster_points[:, feature_2.value],
                    label=f'Cluster: {cluster_idx + 1}')

    plt.title('Cluster Visualization')
    plt.xlabel(str(feature_1))
    plt.ylabel(str(feature_2))
    plt.legend()
    plt.show()


def plot_student_progression(ds_array, feature_1=ErrorTopics.declarations, feature_2=ErrorTopics.array):
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


def plot_errors_ds(ds_array):
    ds_errors_matrix = []

    for i, ds in enumerate(ds_array):
        ds_errors_matrix.append(ds.errors)

    # Calculate cumulative sum of errors for each student
    progression_data = [np.cumsum(student_errors) for student_errors in ds_errors_matrix]
    fig, ax = plt.subplots()

    for idx, progression in enumerate(progression_data):
        ax.plot(progression, label=f"Student {idx + 1}")

    ax.set_xlabel('Error classes')
    ax.set_ylabel('Number of errors')
    plt.title("Errors")
    plt.show()


def plot_warnings_ds(ds_array):
    ds_warnings_matrix = []

    for i, ds in enumerate(ds_array):
        ds_warnings_matrix.append(ds.warnings)

    # Calculate cumulative sum of errors for each student
    progression_data = [np.cumsum(student_errors) for student_errors in ds_warnings_matrix]
    fig, ax = plt.subplots()

    for idx, progression in enumerate(progression_data):
        ax.plot(progression, label=f"Student {idx + 1}")

    ax.set_xlabel('Warnings classes')
    ax.set_ylabel('Number of Warnings')
    plt.title("Warnings")
    plt.show()
