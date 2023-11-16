from models.DevelopmentProcess import DevelopmentProcess
from models.DevelopmentSession import DevelopmentSession
from db.sqlite import SQLiteManager
from utils.plotHelper import plot_student_progression_two_features


SQLiteManager.connect()
errors = SQLiteManager.getErrorsByExamWithStudentId()

dp_array = []
ds_array = []

for error in errors:
    # (exam, class, student_id, number_of_errors)
    found_ds = next((x for x in ds_array if x.exam_id == error[0]), None)
    if found_ds:
        found_ds.update_errors_with_student_id(error)
    else:
        ds = DevelopmentSession(error[0], error[2])
        ds.update_errors_with_student_id(error)
        ds_array.append(ds)

# for ds in ds_array:
#     print('Student Id: ' + str(ds.student_id) + ' exam_id:' + str(ds.exam_id) + ' Errors: ' + str(ds.errors))


# Ho creato i development session come prima, ora li vado a raggruppare per student_id
for ds in ds_array:
    found_dp = next((x for x in dp_array if x.student_id == ds.student_id), None)
    if found_dp:
        found_dp.development_sessions.append(ds)
    else:
        new_dp = DevelopmentProcess(ds.student_id)
        new_dp.development_sessions.append(ds)
        dp_array.append(new_dp)

# for dp in dp_array:
#     print('Student Id: ' + str(dp.student_id) + ' questi sono i miei development process')
#     for ds in dp.development_sessions:
#         print('Student Id: ' + str(ds.student_id) + ' exam_id:' + str(ds.exam_id) + ' Errors: ' + str(ds.errors))
#
for dp in dp_array:
    if len(dp.development_sessions) > 2:
        plot_student_progression_two_features(dp.development_sessions, dp.student_id, "")


# Ho notato che nel database ci sono molte prove replicate, dello stesso studente
# ma con development sessions identiche

