import numpy as np
import matplotlib.pyplot as plt


def plot_errors_dp(dp_array):
    dp_errors_matrix = []

    for i, dp in enumerate(dp_array):
        dp_errors_matrix.append(dp.errors)

    # Print Matrix
    # for row in range(len(dp_errors_matrix)):
    #     for column in range(len(dp_errors_matrix[0])):
    #         print(dp_errors_matrix[row][column], end=" ")
    #     print()

    # Calculate cumulative sum of errors for each student
    progression_data = [np.cumsum(student_errors) for student_errors in dp_errors_matrix]
    fig, ax = plt.subplots()

    for idx, progression in enumerate(progression_data):
        ax.plot(progression, label=f"Student {idx + 1}")

    ax.set_xlabel('Error classes')
    ax.set_ylabel('Number of errors')
    plt.title("Errors")

    plt.show()


def plot_warnings_dp(dp_array):
    dp_warnings_matrix = []

    for i, dp in enumerate(dp_array):
        dp_warnings_matrix.append(dp.warnings)

    # Print Matrix
    # for row in range(len(dp_warnings_matrix)):
    #     for column in range(len(dp_warnings_matrix[0])):
    #         print(dp_warnings_matrix[row][column], end=" ")
    #     print()

    # Calculate cumulative sum of errors for each student
    progression_data = [np.cumsum(student_errors) for student_errors in dp_warnings_matrix]
    fig, ax = plt.subplots()

    for idx, progression in enumerate(progression_data):
        ax.plot(progression, label=f"Student {idx + 1}")

    ax.set_xlabel('Warnings classes')
    ax.set_ylabel('Number of Warnings')
    plt.title("Warnings")

    plt.show()
