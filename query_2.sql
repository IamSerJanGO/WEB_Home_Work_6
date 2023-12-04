SELECT students.id, students.full_name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE grades.subject_id = %s
GROUP BY students.id, students.full_name
ORDER BY avg_grade DESC
LIMIT 1;