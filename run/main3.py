from models.DevelopmentCompilation import DevelopmentCompilation
from models.DevelopmentCompilationProcess import DevelopmentCompilationProcess
from db.sqlite import SQLiteManager
from utils.plotHelper import plot_student_progression


SQLiteManager.connect()
errors = SQLiteManager.getErrorsByCompilation()

dpc_array = []
dc_array = []

for error in errors:
    # (exam, compilation_id, class, number_of_errors)
    found_dc = next((x for x in dc_array if x.compilation_id == error[1]), None)
    if found_dc:
        found_dc.update_errors_array(error)
    else:
        dc = DevelopmentCompilation(error[1], error[0])
        dc.update_errors_array(error)
        dc_array.append(dc)

# for dc in dc_array:
#     print('Exam_id:' + str(dc.exam_id) + ' Compilation_id:' + str(dc.compilation_id) + ' Errors: ' + str(dc.errors))

for dc in dc_array:
    found_dp = next((x for x in dpc_array if x.exam_id == dc.exam_id), None)
    if found_dp:
        found_dp.development_compilations.append(dc)
    else:
        new_dp = DevelopmentCompilationProcess(dc.exam_id)
        new_dp.development_compilations.append(dc)
        dpc_array.append(new_dp)

for dp in dpc_array:
    print('Exam Id: ' + str(dp.exam_id) + ' questi sono i miei development process')
    for dc in dp.development_compilations:
        print('Exam_id:' + str(dc.exam_id) + ' Compilation Id: ' + str(dc.compilation_id) + ' lines: ' + str(dc.lines) + ' Errors: ' + str(dc.errors))


# for dpc in dpc_array:
#     if len(dpc.development_compilations) > 2:
#         plot_student_progression(dpc.development_compilations)
#
