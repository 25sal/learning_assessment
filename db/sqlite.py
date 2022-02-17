import sqlite3


class SQLiteManager:
    conn = None

    @classmethod
    def connect(cls, db="elpro.db"):
        cls.conn = sqlite3.connect(db)

    @classmethod
    def getSessionID(cls,  session):
        sql = "SELECT id FROM sessions where date='" + session + "'"
        cur = cls.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        else:
            return -1

    @classmethod
    def addSession(cls, session, is_exam):
        sessionID = cls.getSessionID(session)
        if sessionID > 0:
            return sessionID;
        sql = "INSERT INTO sessions (id,date,isexam) VALUES(NULL,?,?)"
        cur = cls.conn.cursor()
        if is_exam:
            cur.execute(sql, (session, 1))
        else:
            cur.execute(sql, (session, 0))
        return cur.lastrowid


    @classmethod
    def getStudentID(cls, matr):
        sql = "SELECT id FROM students where matr='" + matr + "'"
        cur = cls.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        else:
            return -1

    @classmethod
    def insertStudent(cls, matr):
        sql = "INSERT INTO students  VALUES(NULL,?)"
        cur = cls.conn.cursor()
        parameter = (str(matr),)
        cur.execute(sql, parameter)
        cls.conn.commit()
        return cur.lastrowid

    @classmethod
    def getExamID(cls, studentID, sessionID):
        sql = "SELECT id FROM exams where student=? and session=?"
        cur = cls.conn.cursor()
        cur.execute(sql, (studentID, sessionID,))
        rows = cur.fetchall()
        if len(rows) > 0:
            return rows[0][0]
        else:
            return -1

    @classmethod
    def insertExam(cls, studentID, sessionID):
        sql = "INSERT INTO exams  VALUES(NULL,?,?)"
        cur = cls.conn.cursor()
        cur.execute(sql, (studentID, sessionID,))
        cls.conn.commit()
        return cur.lastrowid

    @classmethod
    def insertCompilation(cls, compout, examID):
        sql = "INSERT INTO compilations(id,exam, success,datetime) VALUES(NULL, ?, ?,?)";
        if compout.success:
            success = 1
        else:
            success = 0
        cur = cls.conn.cursor()
        cur.execute(sql, (examID, success, compout.comp_time,))

        last_id = cur.lastrowid
        sql = "INSERT INTO compilerlogs(compilationid, seq, type, row,col,log) VALUES(?, ?, ?,?,?,?)"
        i = 0
        for log in compout.logs:
            try:
                cur.execute(sql, (last_id, i, log.typ, log.row, log.col, log.log,))
                i += 1
            except sqlite3.IntegrityError as e:
                pass
