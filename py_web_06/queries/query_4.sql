-- Find the average grade point average of a stream (across the grade table)

SELECT ROUND(AVG(grades.grade), 2) AS all_students_avg_grade
FROM grades
ORDER BY all_students_avg_grade
