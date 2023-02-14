-- The scores of students in a particular group in a particular course in the last class

SELECT gr.group_name AS group_name, s.student AS student, sub.subject AS subject,
      g.grade AS grade, g.created_at AS last_lesson_date
FROM grades g
INNER JOIN students s ON g.student_id = s.id
INNER JOIN groups gr ON s.group_id = gr.id
INNER JOIN subjects sub ON sub.id = g.subject_id
WHERE gr.id = 2
AND sub.id = 1
AND last_lesson_date in (SELECT MAX(g.created_at)
						 FROM grades g
                         INNER JOIN students s ON g.student_id = s.id
                         INNER JOIN groups gr ON s.group_id = gr.id
                         INNER JOIN subjects sub ON sub.id = g.subject_id
                         WHERE gr.id = 2 AND sub.id = 1)