import sqlite3

conn_plain = None
con_an = None
try:
    conn_plain = sqlite3.connect("elpro.db")
    conn_an = sqlite3.connect("elprotest.db")
    # print(sqlite3.version)
except sqlite3.Error as e:
    print(e)

cur_plain = conn_plain.cursor()
cur_an = conn_an.cursor()

sql = "select count(*) from sessions"

result = cur_plain.execute(sql)
rows = result.fetchall()
plain_sessions = rows[0][0]

result = cur_an.execute(sql)
rows = result.fetchall()
an_sessions = rows[0][0]
print("plain vs anonymized")
print("sessions: " + str(plain_sessions) + " vs " + str(an_sessions))


sql = "select count(*) from exams"

result = cur_plain.execute(sql)
rows = result.fetchall()
plain_sessions = rows[0][0]

result = cur_an.execute(sql)
rows = result.fetchall()
an_sessions = rows[0][0]

print("students: " + str(plain_sessions) + " vs " + str(an_sessions))
