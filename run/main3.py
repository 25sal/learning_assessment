from models.DevelopmentCompilation import DevelopmentCompilation
from models.DevelopmentCompilationProcess import DevelopmentCompilationProcess
from db.sqlite import SQLiteManager
from utils.plotHelper import plot_compilations_all_features, plot_compilations_all_features_normalized, plot_compilations_all_features_with_lines

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

for dc in dc_array:
    dc.normalize_errors()

# for dc in dc_array:
#     print('Exam_id:' + str(dc.exam_id) + ' Compilation_id:' + str(dc.compilation_id) + ' Errors: ' + str(dc.errors))

for dc in dc_array:
    found_dc = next((x for x in dpc_array if x.exam_id == dc.exam_id), None)
    if found_dc:
        found_dc.development_compilations.append(dc)
    else:
        new_dpc = DevelopmentCompilationProcess(dc.exam_id)
        new_dpc.development_compilations.append(dc)
        dpc_array.append(new_dpc)

# for dp in dpc_array:
#     print('Exam Id: ' + str(dp.exam_id) + ' questi sono i miei development process')
#     for dc in dp.development_compilations:
#         print('Exam_id:' + str(dc.exam_id) + ' Compilation Id: ' + str(dc.compilation_id) + ' lines: ' + str(dc.lines) + ' Errors: ' + str(dc.errors))


for dpc in dpc_array:
    plot_compilations_all_features(dpc.development_compilations, dpc.exam_id, "/Users/leobartowski/Documents/Tesi/Plots/Compilations/AllFeatures/")
    plot_compilations_all_features_normalized(dpc.development_compilations, dpc.exam_id, "/Users/leobartowski/Documents/Tesi/Plots/Compilations/AllFeaturesNormalized/")
    plot_compilations_all_features_with_lines(dpc.development_compilations, dpc.exam_id, "/Users/leobartowski/Documents/Tesi/Plots/Compilations/AllFeaturesWithLines/")

