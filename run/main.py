from ml.my_k_means import my_k_means
from models.DevelopmentSession import DevelopmentSession
from db.sqlite import SQLiteManager
from models.enums import ErrorType
from utils.plotHelper import plot_radar_all_centroid_same_plot, plot_radar_all_centroid_different_plot

# ! Recap di quello che ho fatto:
# Utilizzando le query ho creato delle tabelle che mi contassero quanti elementi ogni exam
# avesse di una specifica classe (ex. exam_id = 432 ha 10 errori di classe 6)
# data la struttura dati che mi ritorna sqlite.py [(4667, 0, 1), (4667, 5, 1), (4667, 6, 10),...]
# sono andato a estrapolare il secondo (classe dell'errore e il terzo elemento (count di quanti sono di quella classe)
# e ho sovrascritto l' array di tutti 0 che ho creato
# per poter aggiungere tutti gli errori allo stesso oggetto non credo un nuovo dp per ogni elemento della tabella
# ma controllo prima se esista un elemento con lo stesso exam_id, in caso positivo sovrascrivo solo
# quello che mi serve altrimenti creo un nuovo elemento
# Ragionamento identico per i warning
# RISULTATO -> Ho un array di dp che hanno nel vettore quello che mi serve, cioè quanti errori e warning
# e di quale classe sono

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

# m(errors_matrix)
# my_k_means(normalized_errors_matrix)


# plot_radar_all_centroid_same_plot(True)  # Normalized
# plot_radar_all_centroid_same_plot(False)  # Not Normalized

# plot_radar_all_centroid_different_plot(True)
plot_radar_all_centroid_different_plot(False)

# KMeans Warning
# warnings_matrix = []
# for dp in dp_array:
#     warnings_matrix.append(dp.warnings)
#
# my_k_means(warnings_matrix)
