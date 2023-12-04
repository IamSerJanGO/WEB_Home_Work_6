
import psycopg2
from  psycopg2 import DatabaseError

from datetime import datetime, timedelta
import logging

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='123321',
    host="localhost",
    port="5432"
)

cur = conn.cursor()
id_предмету = 1

def read_query(num):
    with open(f'query_{num}.sql', 'r', encoding='utf-8') as file:
        query = file.read()
    return query

query_input = input('Введите число от 1 до 10')

if query_input in ('1', '4', '8'):
    cur.execute(read_query(query_input))
    rows_query = cur.fetchall()

    for row in rows_query:
        print(row)


elif query_input in ('2', '3', '5', '6', '9'):
    cur.execute(read_query(query_input), (input('Введите данные для фильтра'),))
    rows_query = cur.fetchall()

    for row in rows_query:
        print(row)

else:
    cur.execute(read_query(query_input), (input('Введите данные для фильтра'), input('Введите данные для фильтра')))
    rows_query = cur.fetchall()

    for row in rows_query:
        print(row)



