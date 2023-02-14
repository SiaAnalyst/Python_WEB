-- Find a list of students in a particular group

SELECT groups.group_name, students.student
FROM students
INNER JOIN groups ON students.group_id = groups.id
WHERE groups.group_name = "hK-45"
