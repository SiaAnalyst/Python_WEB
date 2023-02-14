-- Find a list of courses a particular student is taking

SELECT DISTINCT students.student, subjects.subject
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subjects.id
WHERE students.student = "Kenneth Snyder"
ORDER BY subjects.subject