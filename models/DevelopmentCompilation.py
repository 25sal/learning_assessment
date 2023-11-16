from models.enums import ErrorType, Grade


class DevelopmentCompilation:

    def __init__(self, compilation_id, exam_id, student_id=0):
        self.compilation_id = compilation_id
        self.exam_id = exam_id
        self.student_id = student_id
        self.lines = 0
        # declaration, conflict, incompatibility, assignment, initialization, parameters, syntax, array/struct
        self.errors = [0, 0, 0, 0, 0, 0, 0, 0]
        self.normalized_errors = []
        # conflict, pointers, cast, scope, conversion, format, syntax, array/struct,
        self.warnings = [0, 0, 0, 0, 0, 0, 0, 0]
        self.results = Grade.INSUF

    def normalize_errors(self):
        for error in self.errors:
            self.normalized_errors.append(error / self.lines)

    def update_errors_array(self, element):
        # ex: [(3, 3, 4, 10), (4, 4, 3, 2),.. -> (exam, compilation_id, class, row, number_of_errors)
        type_of_error_index = element[2]
        self.errors[type_of_error_index] = element[4]
        # This if is need to ensure that we use the highest value of row (lines of code) of the compilation
        if self.lines < element[3]:
            self.lines = element[3]

