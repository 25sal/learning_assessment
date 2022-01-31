import logging
import glob
import os
import re
import shutil
from db.sqlite import SQLiteManager

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class CompilerLog:
    log_types = {"ERROR": 0, "WARNING": 1, "NOTE": 2, "UNDEFINED": -1}

    def __init__(self, col, row, typ, log):
        self.col = col
        self.row = row
        self.typ = typ
        self.log = log
        if typ.upper() in self.log_types.keys():
            self.logtype = self.log_types[typ.upper()]
        else:
            self.logtype = -1

    def __str__(self):
        return str(self.row) + ":" + str(self.col) + ": " + str(self.typ) + " " + self.log


class CompilerOutput:
    student = None
    comp_time = None
    success = True
    logs = None

    def __init__(self, std, cmp_time, succ):
        self.student = std
        self.comp_time = cmp_time
        self.success = succ


class ParseGCCOutput:

    @classmethod
    def parse(cls, folder, filter="20", db="elpro.db"):
        SQLiteManager.connect(db)
        sessions = glob.glob(folder + "/"+filter+"*")
        for session in sessions:
            if os.path.isdir(session):
                session_name = os.path.basename(session)
                logger.info("Processing " + os.path.basename(session))
                sessionID = SQLiteManager.addSession(session_name, True)
                if os.path.isdir(session + "/users/compile"):
                    error_logs = glob.glob(session + "/users/compile/error*")
                    for error_file in error_logs:
                        compiler_output = cls.parse_errors(error_file)
                        student_id = SQLiteManager.getStudentID(compiler_output.student)
                        if student_id < 0:
                            student_id = SQLiteManager.insertStudent(compiler_output.student)
                        exam_id = SQLiteManager.getExamID( student_id, sessionID)
                        if exam_id < 0:
                            exam_id = SQLiteManager.insertExam( student_id, sessionID)
                        SQLiteManager.insertCompilation(compiler_output, exam_id)

                    success_logs = glob.glob(session + "/users/compile/ok*")
                    for success_file in success_logs:
                        compiler_output = cls.parse_success(success_file)
                        student_id = SQLiteManager.getStudentID( compiler_output.student)
                        if student_id < 0:
                            student_id = SQLiteManager.insertStudent( compiler_output.student)
                        exam_id = SQLiteManager.getExamID( student_id, sessionID)
                        if exam_id < 0:
                            exam_id = SQLiteManager.insertExam( student_id, sessionID)
                        elif exam_id == 4:
                            logger.info(logging.WARNING, "exam 4")
                        SQLiteManager.insertCompilation( compiler_output, exam_id)

    @classmethod
    def parse_errors(cls, filename):
        logger.info("Parsing" + filename)
        tokens = os.path.basename(filename).split("_")
        compiler_output = CompilerOutput(tokens[1], int(tokens[2]), False)
        infile = open(filename, "r")
        lines = infile.readlines()
        error_logs = []
        log_expression = re.compile(r'c:(\d+):(\d+): (\w+): (.*)')
        for line in lines:
            if len(line.strip()) > 0:
                '''
                c: parola che cerchiamo, 
                (\\d+) uno o more numero da 0 a 9, 
                (\\w+) prima parola, 
                (.*)  tutte le altre parole
                '''
                result = log_expression.search(line)
                if result is not None:
                    if len(result.groups()) > 0:
                        error_log = CompilerLog(int(result.group(1)), int(result.group(2)), result.group(3),
                                                result.group(4))
                        logger.debug("mat: " + str(error_log))
                        error_logs.append(error_log)
        compiler_output.logs = error_logs
        return compiler_output

    @classmethod
    def parse_success(cls, filename):
        temp = ParseGCCOutput.parse_errors(filename)
        temp.success = True
        return temp


if __name__ == "__main__":
    shutil.copy("elpro_schema.db", "elprotest.db")
    ParseGCCOutput.parse("/home/salvatore/eclipse-workspace/elpro/data/anonymized", "20", "elprotest.db")
