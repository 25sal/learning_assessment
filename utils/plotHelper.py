import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from models.enums import ErrorType
from collections import defaultdict
import matplotlib.ticker as mtick

def plot_radar_node(normalized_errors_ahp, errors, exam_id):
    categories = ['declaration', 'conflict', 'incompatibility', 'assignment', 'initialization', 'parameters', 'syntax', 'array']

    num_features = len(categories)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()
    normalized_errors_ahp = np.append(normalized_errors_ahp, normalized_errors_ahp[0])
    errors = np.append(errors, errors[0])
    angles.append(angles[0])

    ax.fill(angles, normalized_errors_ahp, alpha=0.25, color='r')
    ax.plot(angles, normalized_errors_ahp, label=f'AHP Evaluation: {exam_id}', color='r')
    ax.fill(angles, errors, alpha=0.25, color='b')
    ax.plot(angles, errors, label=f'Errors: {exam_id}', color='b')

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.yaxis.grid(True)

    plt.legend(bbox_to_anchor=(1.1, 1), borderaxespad=0)
    plt.title(f'Grafico radar AHP esame {exam_id}')
    path = 'AHPArticle/Plots/RadarAHP/'
    plt.savefig(path + str(exam_id) + '.png',
                dpi=300,
                )
def plot_radar_ahp(normalized_errors_ahp, exam_id):

    categories = ['declaration', 'conflict', 'incompatibility', 'assignment', 'initialization', 'parameters', 'syntax', 'array']

    num_features = len(categories)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()
    normalized_errors_ahp = np.append(normalized_errors_ahp, normalized_errors_ahp[0])
    angles += angles[:1]

    ax.fill(angles, normalized_errors_ahp, alpha=0.25, color='r')
    ax.plot(angles, normalized_errors_ahp, label=f'Valutazione esame n: {exam_id}', color='r')
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.yaxis.grid(True)

    plt.legend(bbox_to_anchor=(1.1, 1), borderaxespad=0)
    plt.title(f'Grafico radar AHP esame {exam_id}')
    path = '/Users/leobartowski/Documents/Tesi/Plots/RadarAHP/'
    plt.savefig(path + str(exam_id) + '.png',
                dpi=300,
                )


def plot_radar_all_centroid_same_plot(normalized):

    labels = ['declaration', 'conflict', 'incompatibility', 'assignment', 'initialization', 'parameters', 'syntax', 'array']
    centroids_not_normalized = [
        [4.28571429e-01, 1.53846154e-01, 1.20879121e-01, 6.59340659e-02, 2.19780220e-02, 8.79120879e-02, 1.37362637e+00, 3.62637363e-01],
        [2.50000000e+00, 1.00000000e-01, 0.00000000e+00, -1.38777878e-17, -3.46944695e-18, 1.00000000e-01, 1.52000000e+01, 6.00000000e-01],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 6.40000000e+01, 0.00000000e+00],
        [2.17391304e+00, 2.17391304e-01, 2.60869565e-01, 2.17391304e-01, -1.38777878e-17, 3.47826087e-01, 6.95652174e+00, 3.47826087e-01],
        [0.00000000e+00, 2.77555756e-17, 3.33333333e-01, 6.66666667e-01, 0.00000000e+00, 3.33333333e-01, 4.66666667e+00, 8.00000000e+00],
        [0.00000000e+00, 2.77555756e-17, 0.00000000e+00, 0.00000000e+00, 6.66666667e-01, 8.00000000e+00, 8.33333333e+00, 1.11022302e-16]
    ]
    centroids_normalized = [
        [8.69330905e-03, 2.01930454e-03, 9.00613183e-04, 1.73472348e-18, 5.74712644e-04, 7.84574346e-03, 1.00228686e-01, 2.45224814e-03],
        [5.19015660e-03, -4.33680869e-19, 0.00000000e+00, 0.00000000e+00, 1.08420217e-19, 8.67361738e-19, 3.46773197e-01, 2.22222222e-03],
        [8.43609959e-02, 4.01074252e-03, 4.72626602e-03, 5.60797058e-03, 1.08420217e-19, 9.96589940e-03, 4.71099329e-02, 1.40646976e-03],
        [1.78571429e-02, 8.92857143e-03, 0.00000000e+00, 0.00000000e+00, 5.42101086e-20, 2.08333333e-03, 3.47341954e-02, 1.49527129e-01],
        [4.53875919e-03, 6.16879298e-03, 9.49123636e-03, 6.85428564e-03, 6.87285223e-04, 6.56987021e-03, 1.77807740e-02, 9.28546904e-03],
        [2.08892927e-02, 1.61108838e-03, 4.33680869e-19, -4.33680869e-19, 0.00000000e+00, 6.51890482e-04, 2.02253489e-01, 4.15582033e-03]
    ]

    centroids = centroids_normalized if normalized else centroids_not_normalized
    # Number of features/dimensions
    num_features = len(labels)

    # Function to create a radar chart
    def plot_radar_chart(ax, values, label):
        angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()
        #values += values[:1]
        #angles += angles[:1]
        ax.fill(angles, values, alpha=0.25)
        ax.plot(angles, values, label=label)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        ax.yaxis.grid(True)

    # Create a radar chart for each centroid
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    for idx, centroid in enumerate(centroids):
        plot_radar_chart(ax, centroid, f'Centroide {idx + 1}')

    plt.legend(bbox_to_anchor=(0.86, -0.045), ncol=3)
    plt.title('Grafico radar dei centroidi del kMeans ' + ('Normalizzato' if normalized else ''))
    name = 'Normalized' if normalized else 'NotNormalized'
    path = '/Users/leobartowski/Documents/Tesi/Plots/RadarCentroids/'
    plt.savefig(path + 'AllCentroid' + name + '.png',
                dpi=300,
                bbox_inches="tight")
    plt.show()


def plot_radar_all_centroid_different_plot(centroids,normalized, img_path):

    labels = ['declaration', 'conflict', 'incompatibility', 'assignment', 'initialization', 'parameters', 'syntax', 'array']
    '''
    centroids_not_normalized = [
        [4.28571429e-01, 1.53846154e-01, 1.20879121e-01, 6.59340659e-02, 2.19780220e-02, 8.79120879e-02, 1.37362637e+00, 3.62637363e-01],
        [2.50000000e+00, 1.00000000e-01, 0.00000000e+00, -1.38777878e-17, -3.46944695e-18, 1.00000000e-01, 1.52000000e+01, 6.00000000e-01],
        [1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 0.00000000e+00, 6.40000000e+01, 0.00000000e+00],
        [2.17391304e+00, 2.17391304e-01, 2.60869565e-01, 2.17391304e-01, 0.00000000e+00, 3.47826087e-01, 6.95652174e+00, 3.47826087e-01],
        [0.00000000e+00, 2.77555756e-17, 3.33333333e-01, 6.66666667e-01, 0.00000000e+00, 3.33333333e-01, 4.66666667e+00, 8.00000000e+00],
        [0.00000000e+00, 2.77555756e-17, 0.00000000e+00, 0.00000000e+00, 6.66666667e-01, 8.00000000e+00, 8.33333333e+00, 1.11022302e-16]
    ]
    

    centroids_normalized = [
        [8.69330905e-03, 2.01930454e-03, 9.00613183e-04, 1.73472348e-18, 5.74712644e-04, 7.84574346e-03, 1.00228686e-01, 2.45224814e-03],
        [5.19015660e-03, -4.33680869e-19, 0.00000000e+00, 0.00000000e+00, 1.08420217e-19, 8.67361738e-19, 3.46773197e-01, 2.22222222e-03],
        [8.43609959e-02, 4.01074252e-03, 4.72626602e-03, 5.60797058e-03, 1.08420217e-19, 9.96589940e-03, 4.71099329e-02, 1.40646976e-03],
        [1.78571429e-02, 8.92857143e-03, 0.00000000e+00, 0.00000000e+00, 5.42101086e-20, 2.08333333e-03, 3.47341954e-02, 1.49527129e-01],
        [4.53875919e-03, 6.16879298e-03, 9.49123636e-03, 6.85428564e-03, 6.87285223e-04, 6.56987021e-03, 1.77807740e-02, 9.28546904e-03],
        [2.08892927e-02, 1.61108838e-03, 4.33680869e-19, -4.33680869e-19, 0.00000000e+00, 6.51890482e-04, 2.02253489e-01, 4.15582033e-03]
    ]
    
    centroids = centroids_normalized if normalized else centroids_not_normalized
    '''

    # Number of features/dimensions
    num_features = len(labels)

    # Function to create a radar chart
    def plot_radar_chart(ax, values, label, color):
        angles = np.linspace(0, 2 * np.pi, num_features, endpoint=False).tolist()
        angles.append(angles[0])
        values=values.tolist()
        values.append(values[0])
        ax.fill(angles, values, alpha=0.25, color=color)
        ax.plot(angles, values, label=label, color=color)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        ax.set_ylim(bottom=-0.001)
        ax.yaxis.grid(True)

    colors = ['b', 'orange', 'g', 'r', 'm', 'brown','k','yellow']
    plt.rcParams.update({'font.size': 16})
    for idx, centroid in enumerate(centroids):
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
        plot_radar_chart(ax, centroid, f'Centroid {idx + 1}', colors[idx])
        # plt.legend(loc='upper right')
        # plt.title(f'Grafico radar del centroide {idx + 1} kMeans')
        folder = 'Normalized/' if normalized else 'NotNormalized/'
        path = img_path+'/RadarCentroids/'
        plt.savefig(path + folder + 'Centroid' + str(idx + 1) + '.png',
                    dpi=300,
                    bbox_inches="tight")


def plot_k_means_based_on_features(data_array,
                                   cluster_labels,
                                   path,
                                   feature_1=ErrorType.declaration,
                                   feature_2=ErrorType.array,
                                   print_multiplicity=True,
                                   num_clusters=6
                                   ):
    plt.figure(figsize=(8, 6))

    # Create a scatter plot for each cluster
    for cluster_idx in range(num_clusters):
        cluster_points = data_array[cluster_labels == cluster_idx]
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        if print_multiplicity:
            plt.scatter(cluster_points[:, feature_1.value],
                        cluster_points[:, feature_2.value],
                        label=f'Cluster: {cluster_idx + 1}',
                        edgecolors=colors[cluster_idx],
                        facecolors='none',
                        )
        else:
            plt.scatter(cluster_points[:, feature_1.value],
                        cluster_points[:, feature_2.value],
                        label=f'Cluster: {cluster_idx + 1}',
                        )

    if print_multiplicity:
        coord_counts = defaultdict(int)
        for coord, label in zip(data_array, cluster_labels):
            coord = [coord[feature_1.value], coord[feature_2.value]]
            coord_str = tuple(coord)
            coord_counts[coord_str] += 1

        for coord, count in coord_counts.items():
            plt.annotate(count, coord, textcoords="offset points", xytext=(0, -2), ha='center', fontsize=5, c='black')

    plt.title('Cluster Visualization for Errors')
    plt.xlabel(str(feature_1))
    plt.ylabel(str(feature_2))
    plt.legend()
    plt.savefig(path + str(
        feature_1) + ' - ' + str(feature_2) + '.png',
                dpi=300,
                bbox_inches="tight")


def plot_student_progression_two_features(ds_array,
                                          exam_id,
                                          path,
                                          feature_1=ErrorType.declaration,
                                          feature_2=ErrorType.array,
                                          ):
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
    # plt.xlabel('Exam IDs')
    plt.ylabel('Value')
    plt.title('Change of ' + str(feature_1) + ' and ' + str(feature_2))
    plt.legend()
    plt.savefig(path + str(exam_id) + ' - ' + str(
        feature_1) + ' - ' + str(feature_2) + ' .png',
                dpi=300,
                bbox_inches="tight")


def plot_student_progression_all_features(development_process, path):
    errors = []
    exam_ids = []
    for ds in development_process.development_sessions:
        exam_ids.append(ds.exam_id)
        errors.append(ds.errors)

    errors = np.array(errors)
    n_exams = list(range(len(exam_ids)))

    # Create a line plot
    plt.figure(figsize=(8, 6))
    plt.plot(n_exams, errors[:, ErrorType.declaration.value], label=str(ErrorType.declaration))
    plt.plot(n_exams, errors[:, ErrorType.conflict.value], label=str(ErrorType.conflict))
    plt.plot(n_exams, errors[:, ErrorType.incompatibility.value], label=str(ErrorType.incompatibility))
    plt.plot(n_exams, errors[:, ErrorType.assignment.value], label=str(ErrorType.assignment))
    plt.plot(n_exams, errors[:, ErrorType.initialization.value], label=str(ErrorType.initialization))
    plt.plot(n_exams, errors[:, ErrorType.parameters.value], label=str(ErrorType.parameters))
    plt.plot(n_exams, errors[:, ErrorType.syntax.value], label=str(ErrorType.syntax))
    plt.plot(n_exams, errors[:, ErrorType.array.value], label=str(ErrorType.array))
    plt.xticks(list(map(int, n_exams)))
    plt.xlabel('exam id')
    plt.ylabel('number of errors')
    plt.title('Errors change based on student progression')
    plt.legend()
    plt.savefig(
        path + 'StudentId-' + str(development_process.student_id) + '.png',
        dpi=300,
        bbox_inches="tight")
    # plt.show()


def plot_student_progression_all_features_normalized(development_process, path):
    errors = []
    exam_ids = []
    for ds in development_process.development_sessions:
        exam_ids.append(ds.exam_id)
        errors.append(ds.normalized_errors)

    errors = np.array(errors)
    n_exams = list(range(len(exam_ids)))

    # Create a line plot
    plt.figure(figsize=(8, 6))
    plt.plot(n_exams, errors[:, ErrorType.declaration.value], label=str(ErrorType.declaration))
    plt.plot(n_exams, errors[:, ErrorType.conflict.value], label=str(ErrorType.conflict))
    plt.plot(n_exams, errors[:, ErrorType.incompatibility.value], label=str(ErrorType.incompatibility))
    plt.plot(n_exams, errors[:, ErrorType.assignment.value], label=str(ErrorType.assignment))
    plt.plot(n_exams, errors[:, ErrorType.initialization.value], label=str(ErrorType.initialization))
    plt.plot(n_exams, errors[:, ErrorType.parameters.value], label=str(ErrorType.parameters))
    plt.plot(n_exams, errors[:, ErrorType.syntax.value], label=str(ErrorType.syntax))
    plt.plot(n_exams, errors[:, ErrorType.array.value], label=str(ErrorType.array))
    plt.xticks(list(map(int, n_exams)))
    plt.xlabel('exam id')
    plt.ylabel('numbers of normalized error')
    plt.title('Normalized errors change based on student progression')
    plt.legend()
    plt.savefig(
        path + 'StudentId-' + str(development_process.student_id) + '.png',
        dpi=300,
        bbox_inches="tight")
    # plt.show()


def plot_compilations_all_features(dc_array, exam_id, path):
    errors = []
    exam_ids = []
    for dc in dc_array:
        exam_ids.append(dc.exam_id)
        errors.append(dc.errors)

    errors = np.array(errors)
    n_exams = list(range(len(exam_ids)))

    # Create a line plot
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(n_exams, errors[:, ErrorType.declaration.value], label=str(ErrorType.declaration))
    plt.plot(n_exams, errors[:, ErrorType.conflict.value], label=str(ErrorType.conflict))
    plt.plot(n_exams, errors[:, ErrorType.incompatibility.value], label=str(ErrorType.incompatibility))
    plt.plot(n_exams, errors[:, ErrorType.assignment.value], label=str(ErrorType.assignment))
    plt.plot(n_exams, errors[:, ErrorType.initialization.value], label=str(ErrorType.initialization))
    plt.plot(n_exams, errors[:, ErrorType.parameters.value], label=str(ErrorType.parameters))
    plt.plot(n_exams, errors[:, ErrorType.syntax.value], label=str(ErrorType.syntax))
    plt.plot(n_exams, errors[:, ErrorType.array.value], label=str(ErrorType.array))
    plt.xticks(list(map(int, n_exams)))
    ax.xaxis.set_major_locator(plt.AutoLocator())
    plt.xlabel('compilation id')
    plt.ylabel('number of errors')
    plt.title('Errors change based on compilations')
    plt.legend(bbox_to_anchor=(0, 1.06, 1, 0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=3)
    plt.savefig(
        path + 'ExamId-' + str(exam_id) + '.png',
        dpi=300,
        bbox_inches="tight")


def plot_compilations_all_features_with_lines(dc_array, exam_id, path):
    errors = []
    exam_ids = []
    lines = []

    for dc in dc_array:
        exam_ids.append(dc.exam_id)
        errors.append(dc.errors)
        lines.append(dc.lines)

    errors = np.array(errors)
    n_exams = list(range(len(exam_ids)))

    fig, ax1 = plt.subplots(figsize=(8, 6))  # Create the figure with the specified size

    # Create a line plot for errors on the primary axis
    ax1.plot(n_exams, errors[:, ErrorType.declaration.value], label=str(ErrorType.declaration))
    ax1.plot(n_exams, errors[:, ErrorType.conflict.value], label=str(ErrorType.conflict))
    ax1.plot(n_exams, errors[:, ErrorType.incompatibility.value], label=str(ErrorType.incompatibility))
    ax1.plot(n_exams, errors[:, ErrorType.assignment.value], label=str(ErrorType.assignment))
    ax1.plot(n_exams, errors[:, ErrorType.initialization.value], label=str(ErrorType.initialization))
    ax1.plot(n_exams, errors[:, ErrorType.parameters.value], label=str(ErrorType.parameters))
    ax1.plot(n_exams, errors[:, ErrorType.syntax.value], label=str(ErrorType.syntax))
    ax1.plot(n_exams, errors[:, ErrorType.array.value], label=str(ErrorType.array))

    # Configure the primary axis
    ax1.set_xlabel('Compilation ID')
    ax1.set_ylabel('Number of Errors')
    ax1.set_title('Errors Change Based on Compilations with lines')
    # ax1.xaxis.set_major_locator(MaxNLocator(25))
    ax1.legend(bbox_to_anchor=(0, 1.06, 1, 0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=3)

    # Create a secondary axis sharing the same x-axis with the primary axis
    ax2 = ax1.twinx()  # Create a twin of the primary axis
    ax2.plot(n_exams, lines, 'y:', label='Lines')  # Plot the lines data on the secondary axis
    ax2.set_ylabel('Number of Lines')
    ax2.legend()

    plt.savefig(
        path + 'ExamId-' + str(exam_id) + '.png',
        dpi=300,
        bbox_inches="tight"
    )


def plot_compilations_all_features_normalized(dc_array, exam_id, path):
    errors = []
    exam_ids = []
    for dc in dc_array:
        exam_ids.append(dc.exam_id)
        errors.append(dc.normalized_errors)

    errors = np.array(errors)
    n_exams = list(range(len(exam_ids)))

    # Create a line plot
    fig, ax = plt.subplots(figsize=(8, 6))
    plt.plot(n_exams, errors[:, ErrorType.declaration.value], label=str(ErrorType.declaration))
    plt.plot(n_exams, errors[:, ErrorType.conflict.value], label=str(ErrorType.conflict))
    plt.plot(n_exams, errors[:, ErrorType.incompatibility.value], label=str(ErrorType.incompatibility))
    plt.plot(n_exams, errors[:, ErrorType.assignment.value], label=str(ErrorType.assignment))
    plt.plot(n_exams, errors[:, ErrorType.initialization.value], label=str(ErrorType.initialization))
    plt.plot(n_exams, errors[:, ErrorType.parameters.value], label=str(ErrorType.parameters))
    plt.plot(n_exams, errors[:, ErrorType.syntax.value], label=str(ErrorType.syntax))
    plt.plot(n_exams, errors[:, ErrorType.array.value], label=str(ErrorType.array))
    plt.xticks(list(map(int, n_exams)))
    # ax.xaxis.set_major_locator(plt.AutoLocator())
    plt.xlabel('compilation id')
    plt.ylabel('normalized number of errors')
    plt.title('Normalized errors change based on compilations')
    plt.legend(bbox_to_anchor=(0, 1.06, 1, 0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=3)
    plt.savefig(
        path + 'ExamId-' + str(exam_id) + '.png',
        dpi=300,
        bbox_inches="tight")
    # plt.show()


def plot_normalized_errors_and_lines(developer_sessions, feature=ErrorType.declaration):
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    for i in range(len(developer_sessions)):
        plt.bar(developer_sessions[i].lines, developer_sessions[i].normalized_errors[feature.value])

    plt.xlabel("lines")
    plt.ylabel("number of normalized" + str(feature))
    plt.savefig("/Users/leobartowski/Documents/Tesi/Plots/ErrorsAndLines/Normalized/" + str(feature) + '.png', dpi=300,
                bbox_inches="tight")
    # plt.show()


def plot_errors_and_lines(developer_sessions, feature=ErrorType.declaration):
    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=90)
    for i in range(len(developer_sessions)):
        plt.bar(developer_sessions[i].lines, developer_sessions[i].errors[feature.value])

    plt.xlabel("lines")
    plt.ylabel("number of " + str(feature))

    plt.savefig("/Users/leobartowski/Documents/Tesi/Plots/ErrorsAndLines/NotNormalized/" + str(feature) + '.png',
                dpi=300, bbox_inches="tight")
    # plt.show()


def plot_error_class(errors, img_path):
    plt.figure()
    fig, ax = plt.subplots(figsize=(8, 7))
    values = errors.sum().values
    ax.bar(errors.columns, 100*values/values.sum())
    ax.yaxis.set_major_formatter(mtick.PercentFormatter())
    ax.set_ylabel("Class size")
    ax.set_ylabel("Error class")
    ax.tick_params(axis='x', labelrotation=45)
    plt.subplots_adjust(bottom=0.15)
    plt.savefig(img_path+"/error_plot.png")