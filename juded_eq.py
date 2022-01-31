import sqlite3
from sqlite3 import Error
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
import numpy as np


def red_calc(red_array):
    red_value = 0
    rep = 0
    for i in range(len(red_array)):
        if red_array[i] > 0:
            rep += 1
        else:
            if rep > 0:
                red_value += (rep*rep)/(rep+1)
                rep = 0
    return red_value


def red_alg(errors1, errors2):
    if errors1 is None or errors2 is None or len(errors1) == 0 or len(errors2) == 0:
        return 0
    r = 0
    for error1 in errors1:
        for error2 in errors2:
            if error1[1] == error2[1]:
                if error1[0] == error2[0]:
                    r += 1
                    errors2.remove(error2)
                    break

    return r

def eq_alg(errors1, errors2):
    eq = 0
    if errors1 is None or errors2 is None or len(errors1)==0 or len(errors2)==0:
        return 0

    for error1 in errors1:
        eq += 2
        same_type = False
        same_location = False
        for error2 in errors2:

            if error1[1] == error2[1] and not same_type:
                eq += 3
                same_type = True
                if error1[0] == error2[0]:
                    eq+=3
                    errors2.remove(error2)
                    break
            elif error1[0] == error2[0]:
                eq += 3
                errors2.remove(error2)
                break



    eq = eq/(8*len(errors1))
    return eq


conn = None
try:
    conn = sqlite3.connect("elpro.db_anonim")
    # print(sqlite3.version)
except Error as e:
    print(e)

cur = conn.cursor()
cur.execute('select id, date from sessions')
sessions = cur.fetchall()
eq_total = 0
session_evaluated = 0
red_session = 0
for session in sessions:
    eq_session = 0
    cur.execute('select id from exams e where e.session='+str(session[0]))
    exams = cur.fetchall()
    eq_evaluated = 0
    for exam in exams:
        red_array = []
        cur.execute('select count(c.id), c.datetime from compilations c where c.success=0 and c.exam =' + str(exam[0]) )
        n_comp = cur.fetchall()
        if n_comp[0][0] > 1:

            exam_eq = 0
            cur.execute('select id, success from compilations c where c.exam =' + str(exam[0]) + ' order by id asc')
            compilations = cur.fetchall()
            e1 = None
            errors1 = None
            errors2 = None
            if len(compilations) > 5 and len(compilations) < 40:

                for i in range(len(compilations)-1):
                    if e1 is None:
                        e1 = compilations[i]
                        if e1[1] == 0:
                            cur.execute('select log, row  from compilerlogs c where c.compilationid='+str(e1[0]))
                            errors1 = cur.fetchall()
                    else:
                        e1 = e2
                        errors1 = errors2

                    e2 = compilations[i+1]
                    if e2[1] == 0:
                        cur.execute('select log, row from compilerlogs c where c.type ="error" and c.compilationid=' + str(e2[0]))
                        errors2 = cur.fetchall()
                    else:
                        errors2 = []

                    exam_eq += eq_alg(errors1, errors2)
                    red_array.append(red_alg(errors1, errors2))
                    # print(exam_eq)
                if len(errors2) > 0 or len(errors1) > 0:
                    eq_evaluated += 1
                    exam_eq /= len(compilations)-1
                    # print(session[0], exam[0], exam_eq, len(compilations))
                    eq_session += exam_eq
                red_session += red_calc(red_array)
    if eq_session > 0:
        print(session[1], eq_session/eq_evaluated, red_session/len(sessions))
        session_evaluated += 1
        eq_total += eq_session/eq_evaluated
print(eq_total/session_evaluated)



