import sqlite3
from sqlite3 import Error
import glob
import shutil
import os

conn = None
try:
    conn = sqlite3.connect("elpro.db")
    # print(sqlite3.version)
except Error as e:
    print(e)

cur = conn.cursor()
cur.execute('select id, date from sessions')
rows = cur.fetchall()
sessions = {}
for row in rows:
    sessions[row[1]] = row[0]

cur.execute('select * from students')
rows = cur.fetchall()
students = {}
for row in rows:
    students[row[1]] = row[0]

session_dirs = glob.glob("/home/salvatore/eclipse-workspace/elpro/data/anonymized/*")

for ses_dir in session_dirs:
    if not os.path.basename(ses_dir) in sessions.keys():
        print(ses_dir, "not found")
    else:
        stud_dirs = glob.glob(ses_dir+"/users/a13*")
        for stud_dir in stud_dirs:
            if os.path.basename(stud_dir) not in students.keys():
                print(stud_dir, "not found")
                shutil.rmtree(stud_dir)
            else:
                print(stud_dir, os.path.dirname(stud_dir)+"/"+str(students[os.path.basename(stud_dir)]))
                shutil.move(stud_dir, os.path.dirname(stud_dir)+"/A13XX"+str(students[os.path.basename(stud_dir)]))

        '''
        Anonymization of compile/exec/compile directory       
        '''
        if os.path.isdir(ses_dir + "/users/compile"):
            logfiles = glob.glob(ses_dir + "/users/compile/*")
            for logfile in logfiles:
                logfile_name = os.path.basename(logfile)
                matr_e = logfile_name.split("_")
                matr_plain = matr_e[1]
                matr_an = 'A13XX' + str(students[matr_plain])
                replace_string = "sed -i 's/\/home\/salvatore\/users\/" + matr_plain + "/users\/" + matr_an + "/g' "+ logfile
                os.system(replace_string)
                shutil.move(logfile, ses_dir + "/users/compile/" + matr_e[0] +"_" + matr_an + "_" +matr_e[2])
        # shutil.move(ses_dir, os.path.dirname(ses_dir)+"/"+str(sessions[os.path.basename(ses_dir)]))






