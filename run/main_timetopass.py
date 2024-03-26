import numpy as np

from ml.my_k_means import my_k_means
from models.DevelopmentSession import DevelopmentSession
from db.sqlite import SQLiteManager
from models.enums import ErrorType
from utils.plotHelper import plot_radar_node, plot_error_class, plot_radar_all_centroid_same_plot, plot_radar_all_centroid_different_plot, plot_radar_ahp
import sys
import pandas as pd

# * 1) Connect with Database
SQLiteManager.connect()
cur = SQLiteManager.conn
sql = 'select multiple_ses_stud.student, exams.id, sessions.date, multiple_ses_stud.cnt, results.grade, grade_sort.id'
sql += ' from results, sessions, multiple_ses_stud, students, exams, grade_sort' 
sql += ' where results.grade=grade_sort.grade and exams.session=sessions.id and' 
sql += ' students.matr like multiple_ses_stud.student and exams.student=students.id and'
sql += ' results.session like sessions.date and results.student like students.matr'
sql += ' order by multiple_ses_stud.student, exams.id'

df = pd.read_sql_query(sql,SQLiteManager.conn)
print(df.head())
#ahp_rows=np.genfromtxt("result.csv")

'''
per ogni exam id calcolare il peso e metterlo in una ulteriore colonna 
per ogni studente calcolare la distanza in sessioni e la distanza in tempo tra prima e ultima sessione
separare quelli che hanno avuto un giudizio positivo da negativo nell'ultima sessione

'''

