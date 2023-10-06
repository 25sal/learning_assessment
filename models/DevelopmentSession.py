class DevelopmentSession:

    def __init__(self, exam_id, student_id=0):
        self.student_id = student_id
        self.exam_id = exam_id
        self.lines = 0
        # declaration, conflict, incompatibility, assignment, initialization, parameters, syntax, array / struct
        self.errors = [0, 0, 0, 0, 0, 0, 0, 0]
        self.normalized_errors = []
        # conflict, pointers, cast, scope, conversion, format, syntax, array / struct,
        self.warnings = [0, 0, 0, 0, 0, 0, 0, 0]

    def normalize_errors(self):
        for error in self.errors:
            self.normalized_errors.append(error / self.lines)

    def update_errors_array_given_element(self, element):
        # ex: [(4667, 0, 100, 1), (4667, 5, 100, 1), (4667, 6, 100, 10),...] -> (exam, class, lines, number_of_errors)
        self.exam_id = element[0]
        type_of_error_index = element[1]
        self.errors[type_of_error_index] = element[3]
        if self.lines == 0:
            self.lines = element[2]

    def update_warnings_array_given_element(self, element):
        # ex: [(4667, 0, 1), (4667, 5, 1), (4667, 6, 10),...]  -> (exam, class, number_of_warnings)
        type_of_warning_index = element[1]
        self.warnings[type_of_warning_index] = element[2]

    def update_errors_array_given_element_with_student_id(self, element):
        # ex: [(4667, 0, 234, 1), (4667, 5,354, 1), (4667, 6, 234, 10),..] -> (exam, class,student_id, number_of_errors)
        type_of_error_index = element[1]
        self.errors[type_of_error_index] = element[3]
