SELECT students.full_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
WHERE students.group_id = %s AND grades.subject_id = %s;