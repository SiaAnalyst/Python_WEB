# Homework #6
## Main task
Implement a database whose schema contains:
- Table of students
- Table of groups
- Table of professors
- Table of subjects, indicating the professor who reads the subject
- Table where each student has grades in the subjects with an indication of when the grade was received

Fill the resulting database with random data (~30-50 students, 3 groups, 5-8 subjects, 3-5 professors, up to 20 grades for each student in all subjects). Use the Faker package to populate it.

Make the following samples from the resulting database:
- Find the 5 students with the highest grade point average in all subjects.
- Find the student with the highest grade point average in a particular subject.
- Find the grade point average in groups in a particular subject.
- Find the average grade point average of a stream (across the grade table).
- Find what courses a particular instructor is reading.
- Find a list of students in a particular group.
- Find the grades of students in a particular group in a particular course.
- Find the average grade given by a particular instructor in a particular course.
- Find a list of courses a particular student is taking.
- Find a list of courses that a particular student is being taught by a particular instructor.

For each query, create a separate file query_number.sql with the query number instead of number. The file contains an SQL instruction that can be executed both in the database terminal and through cursor.execute(sql)

## Additional task
For the additional assignment, make the following queries of increased difficulty:
- The average grade that a particular instructor gives to a particular student.
- The scores of students in a particular group in a particular course in the last class.