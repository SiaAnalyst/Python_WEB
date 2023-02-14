-- Find the average grade given by a particular instructor in a particular course

SELECT p.professor AS professor, s.subject AS subject, ROUND(AVG(g.grade), 2) AS avg_rate
FROM grades AS g
INNER JOIN professors p ON p.id = s.professor_id
INNER JOIN subjects s ON g.subject_id = s.id
WHERE p.id = 5
GROUP BY subject