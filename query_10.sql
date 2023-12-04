SELECT subjects.subject_name
FROM subjects
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON students.id = grades.student_id
WHERE subjects.teacher_id = %s AND students.id = %s;