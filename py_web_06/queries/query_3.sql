-- Find the grade point average in groups in a particular subject

SELECT groups.group_name, subjects.subject, ROUND(AVG(grades.grade), 2) AS avg_rate
FROM grades
INNER JOIN subjects ON grades.subject_id = subject_id
INNER JOIN students ON grades.student_id = students.id
INNER JOIN groups ON students.group_id = groups.id
WHERE subject_id = 3