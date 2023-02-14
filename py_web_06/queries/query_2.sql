-- Find the student with the highest grade point average in a particular subject

SELECT students.student, subjects.subject, grades.grade
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subject_id
WHERE subject_id = 3
GROUP BY students.student
ORDER BY grades.grade DESC
LIMIT 1