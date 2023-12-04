SELECT subjects.id, subjects.subject_name
FROM subjects
WHERE subjects.teacher_id = %s;