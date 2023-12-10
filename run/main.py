from ml.my_k_means import my_k_means
from models.DevelopmentSession import DevelopmentSession
from db.sqlite import SQLiteManager
from models.enums import ErrorType
from utils.plotHelper import plot_radar_all_centroid_same_plot, plot_radar_all_centroid_different_plot


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

# Print relations between number of errors and lines of code, for every kind of error
# for i in range(8):
#     plot_normalized_errors_and_lines(ds_array, ErrorTopics(i))
#     plot_errors_and_lines(ds_array, ErrorTopics(i))

# plot_normalized_errors_and_lines(ds_array)

# my_k_means(errors_matrix)
# my_k_means(normalized_errors_matrix)

# * 5) Plot KMeans Centroids Radar Graphs

# plot_radar_all_centroid_same_plot(True)  # Normalized
# plot_radar_all_centroid_same_plot(False)  # Not Normalized
#
# plot_radar_all_centroid_different_plot(True)
# plot_radar_all_centroid_different_plot(False)

# * 6) AHP



