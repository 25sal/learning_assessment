from models.DevelopmentCompilation import DevelopmentCompilation

from db.sqlite import SQLiteManager
from models.enums import ErrorTopics
from utils.plotHelper import plot_student_progression


SQLiteManager.connect()
errors = SQLiteManager.getErrorsByCompilation()


dpc_array = []
dc_array = []

for error in errors:
    # (exam, compilation_id, class, number_of_errors)
    found_ds = next((x for x in dc_array if x.compilation_id == error[1]), None)
    if found_ds:
        DevelopmentCompilation.update_errors_array_given_element_compilation(found_ds, error)
    else:
        dc = DevelopmentCompilation(error[1], error[0])
        dc.update_errors_array_given_element_compilation(dc, error)
        dc_array.append(dc)

for dc in dc_array:
    print('Exam_id:' + str(dc.exam_id) + ' Compilation_id:' + str(dc.compilation_id) + ' Errors: ' + str(dc.errors))




