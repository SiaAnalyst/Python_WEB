-- Find the grades of students in a particular group in a particular course

SELECT groups.group_name, students.student, grades.grade, subjects.subject
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN groups ON students.group_id = groups.id
INNER JOIN subjects ON grades.subject_id = subjects.id
WHERE groups.group_name = "WJ-80"
AND subjects.subject = "Mathematics"
ORDER BY students.student