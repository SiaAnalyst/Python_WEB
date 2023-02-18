# Homework #7
## Introductory
In this homework assignment, we will continue with the homework from the previous module.

In this homework we will use the postgres database. At the command line, run the Docker container:

`docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres`


Instead of `some-postgres` choose your container name and instead of `mysecretpassword` think of your password to connect to the database

### CAUTION
If you agree with your mentor, and it is technically impossible to use postgres, you can replace it with SQLite

## Steps to do your homework
### First step
Implement your SQLAlchemy models, for the tables:
- Student table
- Groups table
- Faculty table
- A table of subjects with the teacher who reads the subject
- A table where each student has grades for the courses, indicating when the grade was received
### Second Step
Use `alembic` to create migrations in the database.

### Third step
Write the `seed.py` script and fill the resulting database with random data (~30-50 students, 3 groups, 5-8 subjects, 3-5 teachers, up to 20 grades for each student in all subjects). Use `Faker` package to populate. Use SQLAlchemy session engine when filling.

### Fourth step
Make the following selections from the resulting database:
1. Find the 5 students with the highest grade point average in all subjects.
2. Find the student with the highest average score in a particular subject.
3. Find the grade point average in groups in a particular subject.
4. Find the average grade point average of a stream (across the grade table).
5. Find what courses a particular instructor is reading.
6. Find a list of students in a particular group.
7. Find the grades of students in a particular group in a particular course.
8. Find the average grade given by a particular instructor in a particular course.
9. Find a list of courses a particular student is taking.
10. Find a list of courses that a particular student is being taught by a particular instructor.
For queries, make a separate file `my_select.py` with 10 functions from `select_1` to `select_10`. Execution of the function should return a result similar to the previous homework. For queries, use the mechanism of SQLAlchemy sessions.

### Tips and Tricks
This assignment will test your ability to use SQLAlchemy documentation. But we'll give you basic hints and solution directions right away. Suppose we have the following query.

Find the 5 students with the highest grade point average in all subjects.
```    
    SELECT s.fullname, round(avg(g.grade), 2) AS avg_grade
    FROM grades g
    LEFT JOIN students s ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY avg_grade DESC
    LIMIT 5;
```
Let's try to translate it into an ORM SQLAlchemy query. Suppose we have a session in the variable `session`. There are `Student` and `Grade` models described for the corresponding tables. Assume that the database is already populated with data. SQLAlchemy stores aggregation functions in a `func` object. It has to be specially imported `from sqlalchemy import func` and then we can use `func.round` and `func.avg` methods. So the first line of the SQL query should look like this `session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))`. Here we used `label('avg_grade')` so the ORM does the naming of the field, with the grade point average, using the `AS` operator.

Next, `FROM grades g` is replaced by the `select_from(Grade)` method. Replacing `JOIN` statement is easy with the `join(Student)` function and the rest is done by ORM. Group by field with `group_by(Student.id)`.

The `order_by` function is responsible for sorting, by default it sorts as `ASC`, but we obviously need `DESC` ascending mode and by `avg_grade` field that we created in the query. We import `from sqlalchemy import func, desc` and the final look is `order_by(desc('avg_grade'))`. The limit of five values is a function with the same name `limit(5)`. That's it, our query is ready.

The final version of the ORM SQLAlchemy query.
```
session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
```
```
[('Mary Smith', Decimal('8.33')), ('Kimberly Howard', Decimal('8.17')), ('Gregory Graves', Decimal('7.92')), ('Mrs. Diamond Carter', Decimal('7.53')), ('Emma Hernandez', Decimal('7.31'))]
```
The rest of the queries you should build similarly to the above example. One last tip, if you decide to make nested queries, use `scalar-selects`.

## Additional task
### The first part
For the extra assignment, make the following queries of increased difficulty:
1. The average grade that a particular instructor gives to a particular student.
2. The scores of students in a particular group in a particular course in the last class.

### Second part
Instead of the `seed.py` script, think about and implement a full-fledged CLI application for CRUD operations on the database. Use the `argparse` module for this.

Use `--action` command or shortened version of `-a` for CRUD operations. And the `--model (-m)` command to specify which model the operation is performed on.

Example:

- `--action create -m Teacher --name 'Boris Jonson'` create teacher
- `--action list -m Teacher` show all teachers
- `--action update -m Teacher --id 3 --name 'Andry Bezos'` update teacher `id=3`
- `--Remove -m Teacher --id 3` to remove teacher `id=3`
Implement these operations for each model.

#### INFO
Examples of executing commands in the terminal.

Create teacher
```
py main.py -a create -m Teacher -n 'Boris Jonson'
```

Create a group
```
py main.py -a create -m Group -n 'AD-101'
```