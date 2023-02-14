-- The average grade that a particular instructor gives to a particular student

SELECT p.professor AS professor, s.student AS student, ROUND(AVG(g.grade), 2) AS avg_rate
FROM grades g
INNER JOIN subjects sub ON g.subject_id = sub.id
INNER JOIN students s ON s.id = g.student_id
INNER JOIN professors p ON p.id = sub.professor_id
WHERE s.id = 1 AND p.id = 2