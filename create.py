from faker import Faker
import psycopg2
from  psycopg2 import DatabaseError
import random
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
fake = Faker('uk_UA')

gruops = ['Группа 1','Группа 2','Группа 3']
studens_count = random.randint(30, 50)
teachers_count = random.randint(3, 5)
subjects_count = random.randint(5, 8)
# кол-во оценок у кажого студента - реализуем

try:
    for name_gruop in gruops:
        cur.execute('INSERT INTO groups (name) VALUES (%s)', (name_gruop,))
    conn.commit()
except DatabaseError as e:
    conn.rollback()
    logging.error(e)

try:
    for _ in range(subjects_count):
        cur.execute('INSERT INTO subjects (subject_name) VALUES (%s)', (fake.name(),))
    conn.commit()
except DatabaseError as e:
    conn.rollback()
    logging.error(e)

try:
    for _ in range(subjects_count):
        cur.execute('INSERT INTO subjects (subject_name) VALUES (%s)', (fake.name(),))
    conn.commit()
except DatabaseError as e:
    conn.rollback()
    logging.error(e)

try:
    for _ in range(studens_count):
        group = random.randint(1, len(gruops))
        cur.execute('INSERT INTO students (full_name, group_id) VALUES (%s,%s) RETURNING id', (fake.name(), group))
        student_id = cur.fetchone()[0]  # Отримуємо значення id з результату RETURNING

        for sub_id in range(1, subjects_count + 1):
            for _ in range(random.randint(10, 20)):
                grade = random.randint(1, 100)
                date = fake.date_between(start_date='-1y', end_date='today')
                cur.execute('INSERT INTO grades (student_id, subject_id, grade, grade_date) VALUES (%s, %s, %s, %s)',
                            (student_id, sub_id, grade, date))
        conn.commit()
except DatabaseError as e:
    conn.rollback()
    logging.error(e)
finally:
    cur.close()
    conn.close()