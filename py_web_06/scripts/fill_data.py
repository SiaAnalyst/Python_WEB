import faker
from datetime import datetime
from random import randint, choice
import sqlite3


NUMBER_OF_STUDENTS = 45
NUMBER_OF_GROUPS = 3
NUMBER_OF_PROFESSORS = 5
NUMBER_OF_SUBJECTS = 7


def generate_data(num_studs, num_profs, num_groups) -> tuple:
    """
    Generate fake_students, fake_professors, fake_subjects, fake_grades
    returns them
    """
    fake_data = faker.Faker()
    fake_students = [fake_data.name() for _ in range(num_studs)]
    fake_professors = [fake_data.name() for _ in range(num_profs)]
    fake_subjects = [
        "Data science",
        "Mathematics",
        "Statistics",
        "Artificial Intelligence",
        "Machine Learning",
        "Data Warehousing",
        "Python Core",
    ]
    fake_groups = [fake_data.bothify(text="??-##") for _ in range(num_groups)]
    fake_grades = [1, 2, 3, 4, 5]

    return fake_students, fake_professors, fake_subjects, fake_groups, fake_grades


def prepare_data(students, professors, subjects, groups, grades) -> tuple:

    for_students = [(student, randint(1, NUMBER_OF_GROUPS)) for student in students]
    for_professors = [(professor, ) for professor in professors]
    for_subjects = [(subject, randint(1, NUMBER_OF_PROFESSORS)) for subject in subjects]
    for_groups = [(group, ) for group in groups]

    for_grades = []
    for student in students:
        for _ in range(5):
            grade_date = datetime(2022, randint(1, 12), randint(1, 28)).date()
            for_grades.append(
                (
                    randint(1, NUMBER_OF_SUBJECTS),
                    students.index(student) + 1,
                    choice(grades),
                    grade_date,
                )
            )

    return for_students, for_professors, for_subjects, for_groups, for_grades


def insert_data_to_db(students, professors, subjects, groups, grades) -> None:

    with sqlite3.connect("../database/university.db") as con:

        cur = con.cursor()

        sql_to_professors = """
        INSERT INTO professors (professor)
        VALUES (?)
        """
        cur.executemany(sql_to_professors, professors)

        sql_to_subjects = """
        INSERT INTO subjects (subject, professor_id)
        VALUES (?, ?)
        """
        cur.executemany(sql_to_subjects, subjects)

        sql_to_groups = """
        INSERT INTO groups (group_name)
        VALUES (?)
        """
        cur.executemany(sql_to_groups, groups)

        sql_to_students = """
        INSERT INTO students (student, group_id)
        VALUES (?, ?)
        """
        cur.executemany(sql_to_students, students)

        sql_to_grades = """
        INSERT INTO grades (subject_id, student_id, grade, created_at)
        VALUES (?, ?, ?, ?)
        """
        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == "__main__":
    students, professors, subjects, groups, grades = prepare_data(
        *generate_data(
            NUMBER_OF_STUDENTS,
            NUMBER_OF_PROFESSORS,
            NUMBER_OF_GROUPS,
        )
    )
    insert_data_to_db(students, professors, subjects, groups, grades)