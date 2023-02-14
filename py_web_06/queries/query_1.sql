-- Find the 5 students with the highest grade point average in all subjects

SELECT students.student, ROUND(AVG(grades.grade), 2) AS avg_rate
FROM grades
INNER JOIN students ON grades.student_id = students.id
GROUP BY students.student
ORDER BY avg_rate DESC
LIMIT 5