# import pandas as pd
# from word2number import w2n
# import sqlite3 as sql

# l1 = [1,"twenty",13,"eighteen","nine","sixty eight","seventy seven",19]
# l2 = []
# for i in l1:
#     try:
#         l2.append(int(i))
#     except:
#         l2.append(w2n.word_to_num(i))
# print(l2)

# conn = sql.connect('testing.db')
# cursor = conn.cursor()
# cursor.execute("create table if not exists students (student_id int primary key, name varchar(20), age int)")
# # cursor.execute("insert into students values (1,'abc',20),(2,'bcd',21)")
# conn.commit()
# cursor.execute("select * from students")
# print(cursor.fetchall())
# cursor.execute("select * from students where name = ''")
# conn.close()

#Task: create a python script to create a table and insert the data.

# cursor = conn.cursor()
# cursor.execute("create table if not exists users (id integer primary key, name text, description text)")
# cursor.execute("insert into users values (1,'bruce wayne','batman arkham'),(2,'tony stark','ironman avenger')")
# conn.commit()
# cursor.execute("select * from users")
# print(cursor.fetchall())
# conn.close()

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
import pandas as pd
from sqlalchemy.testing.pickleable import User

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"

engine = create_engine('sqlite:///sqlalchemy1.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# new_user = Student(name='Bruce wayne')
# session.add(new_user)
# session.commit()

def new_user(name):
    user = Student(name=name)
    session.add(user)
    session.commit()

# new_user("Jumbo jet")
l3 = ['airbus','mamba','sagarakanya','saahasaveera']
for i in l3:
    new_user(i)
print(session.query(Student.id,Student.name).all())

session.close()

# df = pd.read_sql("select * from student", engine)
# print(df)


# Create a table in sqlalchemy and insert the data from a file into the database table.