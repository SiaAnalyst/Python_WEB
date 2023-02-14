-- Find a list of courses that a particular student is being taught by a particular instructor

SELECT professors.professor, students.student, subjects.subject
FROM grades
INNER JOIN subjects ON grades.subject_id = subjects.id
INNER JOIN students ON grades.student_id = students.id
INNER JOIN professors ON subjects.professor_id = professors.id
WHERE professors.id = 1 AND students.id = 3