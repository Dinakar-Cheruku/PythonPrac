import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlalchemy1.db')
df = pd.read_sql_query("select * from student", conn)
print(df)
