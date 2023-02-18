import sys
import os
from datetime import datetime
from random import randint

from faker import Faker

sys.path.append(os.getcwd())
from database.db_connect import session
from database.models import Professor, Student, Subject, Group, Grade

fake_data = Faker()

NUMBER_GROUPS = 3
NUMBER_STUDENTS = 45
NUMBER_PROFESSORS = 5
NUMBER_SUBJECTS = 7


def create_groups():
    for name in [fake_data.bothify(text="??-##") for _ in range(NUMBER_GROUPS)]:
        group_ = Group(
            group_name=name
        )
        session.add(group_)
    session.commit()


def create_students():
    for _ in range(NUMBER_STUDENTS):
        student = Student(
            student=fake_data.name(),
            group_id=randint(1, NUMBER_GROUPS)
        )
        session.add(student)
    session.commit()


def create_professors():
    for _ in range(NUMBER_PROFESSORS):
        professor = Professor(
            professor=fake_data.name(),
        )
        session.add(professor)
    session.commit()


def create_subjects():
    for subject_name in ["Data science", "Mathematics", "Statistics", "Artificial Intelligence",
                         "Machine Learning", "Data Warehousing", "Python Core"]:
        subject = Subject(
            subject=subject_name,
            professor_id=randint(1, NUMBER_PROFESSORS)
        )
        session.add(subject)
    session.commit()


def create_grades():
    for _ in [1, 2, 3, 4, 5]:
        grade = Grade(
            grade=randint(1, 5),
            created_at=fake_data.date_between_dates(date_start=datetime(2022, 9, 1), date_end=datetime(2023, 1, 1)),
            student_id=randint(1, NUMBER_STUDENTS),
            subject_id=randint(1, NUMBER_SUBJECTS)
        )
        session.add(grade)
    session.commit()


if __name__ == '__main__':
    create_groups()
    create_students()
    create_professors()
    create_subjects()
    create_grades()