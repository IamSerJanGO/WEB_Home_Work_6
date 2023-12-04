
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

try:
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів
    cur.execute('''
        SELECT students.id, students.full_name, AVG(grades.grade) AS avg_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        GROUP BY students.id, students.full_name
        ORDER BY avg_grade DESC
        LIMIT 5;
    ''')
    rows_query_1 = cur.fetchall()
    with open('query_1.sql', 'w', encoding='utf-8') as file:
        for row in rows_query_1:
            file.write(str(row) + '\n')

    # Знайти студента із найвищим середнім балом з певного предмета
    cur.execute('''
        SELECT students.id, students.full_name, AVG(grades.grade) AS avg_grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        WHERE grades.subject_id = %s
        GROUP BY students.id, students.full_name
        ORDER BY avg_grade DESC
        LIMIT 1;
    ''', (id_предмету,))
    rows_query_2 = cur.fetchall()
    with open('query_1.sql', 'w', encoding='utf-8') as file:
        for row in rows_query_2:
            file.write(str(row) + '\n')

    # Додати інші запити тут

    conn.commit()
except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Error: {e}")

try:
    # Знайти середній бал у групах з певного предмета
    cur.execute('''
        SELECT groups.name, AVG(grades.grade) AS avg_grade
        FROM groups
        JOIN students ON groups.id = students.group_id
        JOIN grades ON students.id = grades.student_id
        WHERE grades.subject_id = %s
        GROUP BY groups.name;
    ''', (id_предмету,))
    rows_query_3 = cur.fetchall()
    with open('query_1.sql', 'w', encoding='utf-8') as file:
        for row in rows_query_1:
            file.write(str(row) + '\n')

    # Знайти середній бал на потоці (по всій таблиці оцінок)
    cur.execute('''
        SELECT AVG(grade) AS avg_grade
        FROM grades;
    ''')
    rows_query_4 = cur.fetchall()
    with open('query_4.sql', 'w') as file:
        for row in rows_query_4:
            file.write(str(row) + '\n')

    conn.commit()
except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Error: {e}")

try:
    # Знайти які курси читає певний викладач
    cur.execute('''
        SELECT subjects.subject_name
        FROM subjects
        JOIN teachers ON subjects.teacher_id = teachers.id
        WHERE teachers.full_name = %s;
    ''', (input(),))
    rows_query_5 = cur.fetchall()
    with open('query_5.sql', 'w', encoding='utf-8') as file:
        for row in rows_query_5:
            file.write(str(row) + '\n')

    # Знайти список студентів у певній групі
    cur.execute('''
        SELECT students.full_name
        FROM students
        JOIN groups ON students.group_id = groups.id
        WHERE groups.name = %s;
    ''', (input(),))
    rows_query_6 = cur.fetchall()
    with open('query_6.sql', 'w', encoding='utf-8') as file:
        for row in rows_query_6:
            file.write(str(row) + '\n')

    conn.commit()
except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Error: {e}")

try:
    # Знайти оцінки студентів у окремій групі з певного предмета
    cur.execute('''
        SELECT students.full_name, grades.grade
        FROM students
        JOIN grades ON students.id = grades.student_id
        JOIN subjects ON grades.subject_id = subjects.id
        JOIN groups ON students.gruop_id = groups.id
        WHERE groups.name = 'назва_групи' AND subjects.sumject_name = %s;
    ''', (input("Введіть назву групи: "), input("Введіть назву предмета: ")))
    rows_query_7 = cur.fetchall()
    with open('query_7.sql', 'w') as file:
        for row in rows_query_7:
            file.write(str(row) + '\n')

    conn.commit()
except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Error: {e}")

try:
    # Знайти середній бал, який ставить певний викладач зі своїх предметів
    cur.execute('''
        SELECT teachers.full_name, AVG(grades.grade) AS avg_grade
        FROM teachers
        JOIN subjects ON teachers.id = subjects.teacher_id
        JOIN grades ON subjects.id = grades.subject_id
        GROUP BY teachers.full_name;
    ''')
    rows_query_8 = cur.fetchall()
    with open('query_8.sql', 'w') as file:
        for row in rows_query_8:
            file.write(str(row) + '\n')

    conn.commit()
except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Error: {e}")

try:
    # Знайти список курсів, які відвідує студент
    cur.execute('''
        SELECT subjects.sumject_name
        FROM subjects
        JOIN grades ON subjects.id = grades.subject_id
        JOIN students ON grades.student_id = students.id
        WHERE students.full_name = %s;
    ''', (input(),))
    rows_query_9 = cur.fetchall()
    with open('query_9.sql', 'w') as file:
        for row in rows_query_9:
            file.write(str(row) + '\n')

    conn.commit()

except psycopg2.DatabaseError as e:
    conn.rollback()
    print(f"Error: {e}")

finally:
    cur.close()
    conn.close()