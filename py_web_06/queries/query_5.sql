-- Find what courses a particular instructor is reading

SELECT professors.professor, subjects.subject
FROM subjects
INNER JOIN professors ON subjects.professor_id = professors.id
WHERE professors.professor = "Angela Parrish"