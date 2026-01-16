# print("lorem ipsum bismillah abdhullah")

# for c in range(2,30,4):
#     print(c)
# else:
#     print("done")

# import time
# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         print(a)
#         a, b = b, a + b
#
# s = time.time()
# fib(1000)
# e = time.time()
#
# print(e - s, "seconds")

# Fun learnings

# name = input("Enter you fav char name:")
# age = int(input("Enter your age:"))
# ageH = int(input("Enter ur fav chars age:"))
#
# print(f"Hehehe, you are ",age+ageH," times a bigger idiot than",name)

# x, y = 7,15
# if (x>0 and y<20):print(x,y)
# if (x>0 or y>20):print(x,y)

# if x>0:print("x>0")
# if x<0:print("x<0")
# if y<20:print("y<20")
# else:print("y>20")

# print("x>0" if x > 0 else "", "y<20" if y < 20 else "")


# how many letter that are there
# fruits = ["apple","banana","mango"]
# res = []
# for fruit in fruits:
#     for i in fruit:
#         res.append(i.upper())
# print(res)
# print(len(res))


# print 1 to 5 using for and while

# for i in range(1,6):print(i)

# i=1
# while i<6:
#     print(i)
#     i=i+1

# i=0
# while True:
#     print(i)
#     i=i+1
#     if i==2000:
#         break

# pwd = ''
# while pwd != "123":
#     pwd = input("Enter password (123): ")
# print("access granted")

# inp = int(input("enter a number: "))
# if inp % 2 == 0:print("number is even")
# else:print("number is odd")

# marks = int(input("Enter your marks: "))
# if marks >=90 : print("grade: A")
# elif marks >=80 : print("grade: B")
# elif marks >= 70: print("grade: C")
# else:print("grade: F")

# guessing game
# import random
#
# sn = random.randint(1,10)
# n = 0
# i = 0
# while n!=sn:
#     i += 1
#     n = int(input("Enter your guess btw 1 to 10: "))
#     if n<sn:
#         print("Too low")
#     elif n>sn:
#         print("Too high")
#     else:
#         print("-------------------------")
#         print("you have done it, its ",sn," and you took ",i," guesses")

# item1_price,item2_price,item3_price = 50,120,30
# total_bill = item1_price + item2_price + item3_price
# print(f"The total bill amount is {total_bill}.")

# fruit = ['apple','banana','cherry','date']
# fruit.append('panjandrum')
# fruit.insert(1,'pichafruit')
# print(fruit)
# print(fruit.index('jampandu'))
# print(len(fruit))

# y = [x * x * x for x in range(500) if x % 2 == 0 and x % 19 == 0]
# print(y)
# print(len(y))

# L = [1,2,3,3,3,4,5]
# s = set(L)
# print(s)

# dictionary


# keys = ["name", "age", "grade"]
# values = ["Alex", 21, ['A', 'B', 'A+']]
# student = dict(zip(keys, values))  # use this for production safety.
# student["email"] = "abc@gmail.com"
# student["email"] = "bcd@gmail.com"
# print(student.keys())
# print(student.values())
# print(student.items())
#
# key_list = [x for x in student]
# print(key_list)

# How python is used to create APIs used in analytical dashboards.
# An api is like an interface between the visible dashboards and the curated data. When the dash needs to do some viduslisation it sends a HTTP parameterised request to the python API
# EG: {
#   "start_date": "2026-01-01",
#   "end_date": "2026-01-31",
#   "region": "US"
# }
# Python code:Validates inputs,Applies defaults,Enforces allowed filters,Prevents bad queries
# the python returns
# [
#   {"date": "2026-01-01", "revenue": 12000},
#   {"date": "2026-01-02", "revenue": 13500}
# ]
# Dashboards send parameterized HTTP requests (often JSON). Python APIs validate the request, query curated analytical tables using standardized business logic, and return structured JSON responses consumed by dashboards.

# Example: GET /revenue?start_date=2026-01-01&end_date=2026-01-02
# from fastapi import FastAPI
# from typing import List
#
# app = FastAPI()
#
#
# @app.get("/revenue")
# def get_revenue(start_date: str, end_date: str):
#     """
#     Fetch daily revenue between dates
#     """
#     # Normally this would query Snowflake / BigQuery
#     data = [
#         {"date": "2026-01-01", "revenue": 12000},
#         {"date": "2026-01-02", "revenue": 13500},
#     ]
#
#     return data

#how exactly an sql query goes into this python fucntion. Thats where sql alchemy comes into picture.

# from fastapi import FastAPI
# from sqlalchemy import create_engine, text
#
# app = FastAPI()
#
# engine = create_engine("snowflake://<user>:<password>@<account>/<db>/<schema>")
# @app.get("/revenue")
# def get_revenue(start_date: str, end_date: str):
#
#     query = text("""
#         SELECT
#             date,
#             SUM(revenue) AS revenue
#         FROM gold_daily_revenue
#         WHERE date BETWEEN :start_date AND :end_date
#         GROUP BY date
#         ORDER BY date
#     """)
#
#     with engine.connect() as conn:
#         result = conn.execute(
#             query,
#             {"start_date": start_date, "end_date": end_date}
#         )
#
#         rows = result.fetchall()
#
#     # Convert SQL rows to JSON-friendly format
#     data = [
#         {"date": row.date, "revenue": row.revenue}
#         for row in rows
#     ]
#
#     return data

