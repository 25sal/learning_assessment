class DevelopmentSession:

    def __init__(self, exam_id, student_id=0):
        self.student_id = student_id
        self.exam_id = exam_id
        # declaration, conflict, incompatibility, assignment, initialization, parameters, syntax, array / struct
        self.errors = [0, 0, 0, 0, 0, 0, 0, 0]
        # conflict, pointers, cast, scope, conversion, format, syntax, array / struct,
        self.warnings = [0, 0, 0, 0, 0, 0, 0, 0]

    @classmethod
    def update_errors_array_given_element(cls, development_session, element):
        # ex: [(4667, 0, 1), (4667, 5, 1), (4667, 6, 10),...] -> (exam, class, number_of_errors)
        type_of_error_index = element[1]
        development_session.errors[type_of_error_index] = element[2]

    @classmethod
    def update_warnings_array_given_element(cls, development_session, element):
        # ex: [(4667, 0, 1), (4667, 5, 1), (4667, 6, 10),...]  -> (exam, class, number_of_warnings)
        type_of_warning_index = element[1]
        development_session.warnings[type_of_warning_index] = element[2]

    @classmethod
    def update_errors_array_given_element_with_student_id(cls, development_session, element):
        # ex: [(4667, 0, 234, 1), (4667, 5,354, 1), (4667, 6, 234, 10),..] -> (exam, class,student_id, number_of_errors)
        type_of_error_index = element[1]
        development_session.errors[type_of_error_index] = element[3]

