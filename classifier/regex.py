import re
import logging
import sqlite3

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class ErrorClassifier:
    UNDECLARED = 0
    CONFLICT = 1
    INCOMPATIBILITY = 2
    ASSIGNMENT = 3
    INITIALIZATION = 4
    PARAMETERS = 5
    SYNTAX = 6
    DATA_STRUCT = 7
    categories = ["declaration", "conflict", "incompatibility", "assignment", "initialization",
                  "parameters", "syntax", "array/struct"]

    regex = [
        [".'\\w+'\\s+undeclared", ".invalid\\stype", ".redeclared(.*?)", ".declaration(.*?)but", ".redeclaration"],
        [".(duplicate\\smember)|(conflicting\\stypes)"],
        [".incompatible\\stype"],
        [".assignment"],
        [".parameter\\s'\\w+'\\sis\\sinitialized", ".may\\snot(.*)initialized", ".redefinition(.*?)parameter"],
        [".too\\sfew\\sarguments\\sto\\sfunction\\s'\\w+'", ".too\\smany\\sarguments", ".parameter(.*?)forward"],
        [".expected\\s.", ".empty(.*?)", ".missing(.*?)", ".unknown\\stype\\sname", ".incomplete(.*?)",
         ".else(.*?)without", ".stray(.*?)program"],
        [".array(.*?)", ".struct(.*?)member", ".request\\sfor\\smember\\s'\\w+'"]
    ]


class WarningClassifier:
    CONFLICT = 0
    POINTERS = 1
    CAST = 2
    SCOPE = 4
    FORMAT = 5
    SYNTAX = 6
    ARRAYS = 7

    categories = ["conflict", "pointers", "cast", "scope", "conversion", "format", "syntax", "array/struct"]
    regex = [
        [".conflicting\\stypes"],
        [".incompatible\\s+pointer\\s+type", ".comparison(.*?)pointer", ".pointer(.*?)cast"],
        [".type\\s+defaults"],
        [".scope", ".not\\s+be\\s+visible"],
        [".overflow", ".unknown"],
        [".format(.*?)expects\\s+argument\\s+of\\s+type", ".format(.*?)expects\\s+a\\s+matching(.*?)argument",
         ".too\\s+many\\s+arguments", ".format(.*)string(.*)", ".parameter\\s+names(.*?)type"],
        [".expected\\s.", ".empty(.*?)", ".missing(.*?)",
         ".implicit\\s+declaration", ".multi-character\\s+character"],
        [".array(.*?)will\\s+return", ".excess\\s+elements", ".data\\s+definition"]
    ]


def check_class(classifier, error_class, str_line):
    for i in range(len(classifier.regex[error_class])):
        expression = classifier.regex[error_class][i]
        log_expression = re.compile(expression)
        result = log_expression.search(str_line)
        if result is not None:
            return i
    return -1


def classify_last_errors(db="elpro.db", insert=False):
    conn = sqlite3.connect(db)
    logger.info("DB connected")
    sql = 'SELECT * from last_logs where type="error"'
    '''
    the following evaluate a croudy session with many failures
    sql='select * from last_logs, exams where exams.session=13 and exams.id=last_logs.exam and type="error"'
    '''
    cur = conn.cursor()

    classification = [0] * len(ErrorClassifier.categories)
    unclassified = 0
    # loop through the result set
    result = cur.execute(sql)
    rows = result.fetchall()
    syntax_counters = [0] * len(ErrorClassifier.regex[ErrorClassifier.SYNTAX])
    print("compid, seq, exam, class")
    for row in rows:
        logger.debug("processing " + str(row[5]))
        found = False
        for i in range(len(ErrorClassifier.categories)):
            regex_id = check_class(ErrorClassifier, i, "error: " + str(row[5]))
            if regex_id >= 0:
                found = True
                classification[i] += 1
                if i == ErrorClassifier.SYNTAX:
                    syntax_counters[regex_id] += 1
                print(str(row[0])+","+str(row[1])+","+str(row[6])+","+str(i))
                if insert:
                    query = "INSERT INTO last_errors_class " \
                            "VALUES("+str(row[0])+","+str(row[1])+","+str(row[6])+","+str(i) + ")"
                    cur.execute(query)
                    conn.commit()
                break
                # logger.info(Level.INFO, "Class: " + ErrorClassifier.categories[i] + ": " + str(row[6]))

        if not found:
            unclassified += 1
            logger.debug("category not found" + ": "+str(row[5]))

    for i in range(len(syntax_counters)):
        print(syntax_counters[i])


def classify_last_warnings(db="elpro.db", insert=False):
    conn = sqlite3.connect(db)
    logger.info("DB connected")
    '''
    sql = 'select * from last_logs ll, exams e, sessions s2, compilations c2 where c2.id = ll.compilationid' \
          '  and c2.success =1 and ll.type="warning" and ll.exam= e.id and e.session' \
          ' and e.session =s2.id and s2.date like "2017%"'
    '''
    # sql = "select * from last_logs ll, exams e, sessions s2 where ll.exam= e.id and e.\"session\"
    #        and e.\"session\" =s2.id and s2.date like \"2017%\" and ll.type=\"warning\"";
    sql = 'SELECT * from last_logs, compilations where type="warning" and compilations.id=last_logs.compilationid'

    classification = [0] * len(ErrorClassifier.categories)
    unclassified = 0
    # loop through the result set
    cur = conn.cursor()
    result = cur.execute(sql)
    rows = result.fetchall()
    syntax_counters = [0] * len(ErrorClassifier.regex[ErrorClassifier.SYNTAX])
    print("compid,seq,exam,class")
    for row in rows:
        logger.debug("processing " + str(row[5]))
        found = False
        for i in range(len(WarningClassifier.categories)):
            if check_class(WarningClassifier, i, "error: " + str(row[5])) >= 0:
                if not found:
                    found = True
                    classification[i] += 1
                    print(str(row[0])+","+str(row[1])+","+str(row[6])+","+str(i))
                    if insert:
                        query = "INSERT INTO last_warning_class " \
                                "VALUES(" + str(row[0]) + "," + str(row[1]) + "," + str(row[6]) + "," + str(i) + ")"
                        cur.execute(query)
                        conn.commit()
                    logger.info("Class: " + WarningClassifier.categories[i] + ": " + str(row[5]))
                else:
                    print("overlap: "+WarningClassifier.categories[i]+" ## "+str(row[5]))
        if not found:
            unclassified += 1
            logger.info("category not found"+": "+str(row[5]))


def classify_errors(db="elpro.db", query='SELECT * from compilerlogs where type="error"', insert=False, table="error_class"):
    conn = sqlite3.connect(db)
    logger.info("DB connected")

    cur = conn.cursor()

    classification = [0] * len(ErrorClassifier.categories)
    unclassified = 0
    # loop through the result set
    result = cur.execute(query)
    rows = result.fetchall()
    syntax_counters = [0] * len(ErrorClassifier.regex[ErrorClassifier.SYNTAX])
    print("compid, seq, class")
    for row in rows:
        logger.debug("processing " + str(row[5]))
        found = False
        for i in range(len(ErrorClassifier.categories)):
            regex_id = check_class(ErrorClassifier, i, "error: " + str(row[5]))
            if regex_id >= 0:
                found = True
                classification[i] += 1
                if i == ErrorClassifier.SYNTAX:
                    syntax_counters[regex_id] += 1
                print(str(row[0])+","+str(row[1])+","+str(i))
                if insert:
                    query = "INSERT INTO " + table + " " \
                            "VALUES("+str(row[0])+","+str(row[1])+","+str(i) + ")"
                    cur.execute(query)
                    conn.commit()
                break
                # logger.info(Level.INFO, "Class: " + ErrorClassifier.categories[i] + ": " + str(row[6]))

        if not found:
            unclassified += 1
            logger.debug("category not found" + ": "+str(row[5]))

    for i in range(len(syntax_counters)):
        print(syntax_counters[i])


def classify_warnings(db="elpro.db", query='SELECT * from compilerlogs where type="warning"', insert=False, table="warning_class"):
    conn = sqlite3.connect(db)
    logger.info("DB connected")

    cur = conn.cursor()

    classification = [0] * len(ErrorClassifier.categories)
    unclassified = 0
    # loop through the result set
    result = cur.execute(query)
    rows = result.fetchall()
    syntax_counters = [0] * len(WarningClassifier.regex[WarningClassifier.SYNTAX])
    print("compid, seq, class")
    for row in rows:
        logger.debug("processing " + str(row[5]))
        found = False
        for i in range(len(WarningClassifier.categories)):
            regex_id = check_class(WarningClassifier, i, "error: " + str(row[5]))
            if regex_id >= 0:
                found = True
                classification[i] += 1
                if i == WarningClassifier.SYNTAX:
                    syntax_counters[regex_id] += 1
                print(str(row[0])+","+str(row[1])+","+str(i))
                if insert:
                    query = "INSERT INTO " + table + " " \
                            "VALUES("+str(row[0])+","+str(row[1])+","+str(i) + ")"
                    cur.execute(query)
                    conn.commit()
                break
                # logger.info(Level.INFO, "Class: " + ErrorClassifier.categories[i] + ": " + str(row[6]))

        if not found:
            unclassified += 1
            logger.debug("category not found" + ": "+str(row[5]))

    for i in range(len(syntax_counters)):
        print(syntax_counters[i])


if __name__ == "__main__":
    classify_errors("postcovid.db", insert=True)
    classify_warnings("postcovid.db", insert=True)
    # classify_last_errors("elprotest.db", True)
    # classify_last_warnings("elprotest.db", True)
