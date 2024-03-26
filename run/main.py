import numpy as np

from ml.my_k_means import my_k_means
from models.DevelopmentSession import DevelopmentSession
from db.sqlite import SQLiteManager
from models.enums import ErrorType
from utils.plotHelper import plot_radar_all_centroid_same_plot, plot_radar_all_centroid_different_plot, plot_radar_ahp
import sys 
import pandas as pd

# * 1) Connect with Database
SQLiteManager.connect()
errors = SQLiteManager.getErrorsByExam()
warnings = SQLiteManager.getWarningsByExam()

# * 2) Create dp_array
ds_array = []
for error in errors:
    found_ds = next((x for x in ds_array if x.exam_id == error[0]), None)
    if found_ds:
        found_ds.update_errors(error)
    else:
        development_process = DevelopmentSession(error[0])
        development_process.update_errors(error)
        ds_array.append(development_process)

# for warning in warnings:
#     found_ds = next((x for x in ds_array if x.exam_id == warning[0]), None)
#     if found_ds:
#         DevelopmentSession.update_warnings_array_given_element(found_ds, warning)
#     else:
#         development_process = DevelopmentSession(warning[0])
#         development_process.update_warnings_array_given_element(development_process, warning)
#         ds_array.append(development_process)

for ds in ds_array:
    ds.normalize_errors()


# * 4) Apply KMeans
errors_matrix = []
normalized_errors_matrix = []
for ds in ds_array:
    # if dp.errors != [0, 0, 0, 0, 0, 0, 0, 0]:
    errors_matrix.append(ds.errors)
    normalized_errors_matrix.append(ds.normalized_errors)


labels = ['declaration', 'conflict', 'incompatibility', 'assignment', 'initialization', 'parameters', 'syntax', 'array']
ds = pd.DataFrame(errors_matrix, columns=labels)
#ds['total'] = ds.sum(axis=1)
for label in labels:
    norm = ds[label].max()
    print(label,norm)
    ds[label] = ds[label]/norm

errors_matrix = ds.values.tolist()

ds = pd.DataFrame(normalized_errors_matrix, columns=labels)
for label in labels:
    norm = ds[label].max()
    print(label,norm)
    ds[label] = ds[label]/norm

normalized_errors_matrix = ds.values.tolist()

# Print relations between number of errors and lines of code, for every kind of error
# for i in range(8):
#     plot_normalized_errors_and_lines(ds_array, ErrorTopics(i))
#     plot_errors_and_lines(ds_array, ErrorTopics(i))

# plot_normalized_errors_and_lines(ds_array)

print("not normalized clustering")
centroids = my_k_means(errors_matrix,4)
print("normalized clustering")
norm_centroids = my_k_means(normalized_errors_matrix, 4)

# * 5) Plot KMeans Centroids Radar Graphs
images_path = 'AHPArticle/Plots'
# plot_radar_all_centroid_same_plot(centroids, True,images_path)  # Normalized
# plot_radar_all_centroid_same_plot(False)  # Not Normalized
#

plot_radar_all_centroid_different_plot(norm_centroids,True, images_path)

plot_radar_all_centroid_different_plot(centroids,False, images_path)

# * 6) AHP
'''
ahp_weights = np.array([0.15260589, 0.11779767, 0.10946434, 0.14217351, 0.10818229, 0.11779767, 0.15942134, 0.09255729])

for ds in ds_array:

    norm_errors = np.array(ds.normalized_errors)
    normalized_errors_ahp = norm_errors * ahp_weights
    plot_radar_ahp(normalized_errors_ahp, ds.exam_id)
'''





