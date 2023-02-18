import sys
import os

sys.path.append(os.getcwd())

from database.models import Group, Student, Professor, Subject, Grade
from database.db_connect import session

from sqlalchemy import func, desc, and_


def query_1():
    return session.query(Student.student, func.round(func.avg(Grade.grade), 2).label('avg_rate')).select_from(
        Student).join(
        Grade).filter(Grade.student_id == Student.id).group_by(Student.id).order_by(desc('avg_rate')).limit(5).all()


def query_2():
    return session.query(Student.student, Subject.subject, Grade.grade).select_from(Grade).join(Student,
                                                                                                Subject).filter(
        and_(Student.id == Grade.student_id, Subject.id == Grade.subject_id, Subject.id == 7)).order_by(
        desc(Grade.grade)).limit(1).all()


def query_3():
    return session.query(Group.group_name, func.round(func.avg(Grade.grade), 2)).select_from(Grade).join(Student,
                                                                                                         Subject,
                                                                                                         Group).filter(
        and_(Grade.student_id ==
             Student.id, Subject.id == Grade.subject_id, Group.id == Student.group_id, Subject.id == 3)).group_by(
        Group.group_name).order_by(Group.group_name).all()


def query_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).select_from(Grade).all()


def query_5():
    return session.query(Professor.professor, Subject.subject).select_from(Subject).join(Professor).filter(
        Subject.professor_id == Professor.id).order_by(Professor.professor).all()


def query_6():
    return session.query(Group.group_name, Student.student).select_from(Student).join(Group).filter(
        and_(Student.group_id == Group.id, Group.id == 1)).order_by(
        Student.student).all()


def query_7():
    return session.query(Group.group_name, Student.student, Subject.subject, Grade.grade).select_from(Grade).join(
        Student, Group, Subject).filter(
        and_(Student.group_id == Group.id,
             Student.id == Grade.student_id, Subject.id == Grade.subject_id)).filter(Group.id == 3).filter(
        Subject.id == 4).order_by(desc(Grade.grade)).all()


def query_8():  # some problems
    return session.query(Professor.professor, Subject.subject, func.round(func.avg(Grade.grade), 2)).select_from(
        Grade).join(Professor, Subject).filter(and_(Professor.id == Subject.professor_id,
                                                    Grade.subject_id == Subject.id, Professor.id == 5)).group_by(
        Subject.subject).all()


def query_9():  # .distinct()
    return session.query(Student.student, Subject.subject).select_from(Student).join(Grade, Subject).filter(
        and_(Student.id == Grade.student_id,
             Subject.id == Grade.subject_id, Student.id == 43)).order_by(Subject.subject)


def query_10():
    return session.query(Student.student, Professor.professor, Subject.subject).select_from(Grade).join(
        Subject, Student, Professor).filter(
        and_(Subject.id == Grade.subject_id,
             Student.id == Grade.student_id, Professor.id == Subject.professor_id, Student.id == 42,
             Professor.id == 3)).order_by(Subject.subject).all()


def query_11():
    return session.query(Professor.professor, Student.student, func.round(func.avg(Grade.grade), 2)).select_from(
        Grade).join(Subject, Student, Professor).filter(and_(Subject.id == Grade.subject_id,
                                                             Student.id == Grade.student_id,
                                                             Professor.id == Subject.professor_id,
                                                             Student.id == 2, Professor.id == 2)).group_by(
        Professor.professor, Student.student).all()


def query_12():
    subq = session.query(func.max(Grade.created_at)).select_from(Grade).join(Student, Group, Subject).filter(
        and_(Grade.student_id == Student.id,
             Student.group_id == Group.id, Subject.id == Grade.subject_id, Group.id == 2, Subject.id == 1)).one()

    return session.query(Group.group_name, Student.student, Subject.subject, Grade.grade,
                         Grade.created_at).select_from(Grade, Student, Group, Subject).filter(
        and_(Grade.student_id == Student.id,
             Student.group_id == Group.id, Subject.id == Grade.subject_id, Group.id == 2, Subject.id == 1,
             Grade.created_at.in_(subq))).all()


for r in query_12():
    print(r)
