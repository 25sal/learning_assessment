from PyFiles.my_k_means import my_k_means
from data_structures.DevelopmentSession import DevelopmentProcess
from db.sqlite import SQLiteManager
from utils.plotHelper import plot_errors_dp, plot_warnings_dp

# ! Recap di quello che ho fatto:
# Utilizzando le query ho creato delle tabelle che mi contassero quanti elementi ogni exam
# avesse di una specifica classe (ex. exam_id = 432 ha 10 errori di classe 6)
# data la struttura dati che mi ritorna sqlite.py [(4667, 0, 1), (4667, 5, 1), (4667, 6, 10),...]
# sono andato a estrapolare il secondo (classe dell'errore e il terzo elemento (count di quanti sono di quella classe)
# e ho sovrascritto l'array di tutti 0 che ho creato
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
dp_array = []
for error in errors:
    found_dp = next((x for x in dp_array if x.student_id == error[0]), None)
    if found_dp:
        DevelopmentProcess.update_errors_array_given_element(found_dp, error)
    else:
        development_process = DevelopmentProcess(error[0])
        development_process.update_errors_array_given_element(development_process, error)
        dp_array.append(development_process)

for warning in warnings:
    found_dp = next((x for x in dp_array if x.student_id == warning[0]), None)
    if found_dp:
        DevelopmentProcess.update_warnings_array_given_element(found_dp, warning)
    else:
        development_process = DevelopmentProcess(warning[0])
        development_process.update_warnings_array_given_element(development_process, warning)
        dp_array.append(development_process)

print('dp_array_len: ' + str(len(dp_array)))
for dp in dp_array:
    print('exam_id: ' + str(dp.student_id) + ' errors: ' + str(dp.errors) + ' warnings: ' + str(dp.warnings))

# * 3) Plot db_array
plot_errors_dp(dp_array)
plot_warnings_dp(dp_array)

# * 4) Apply KMeans
# errors_matrix = []
# for dp in dp_array:
#     errors_matrix.append(dp.errors)

# my_k_means(errors_matrix)





