from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_name = Column(String(150), nullable=False)

    students = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey('groups.id', ondelete="CASCADE"))

    group = relationship('Group', back_populates='students')
    grades = relationship('Grade', back_populates='student')


class Professor(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True)
    professor = Column(String(150), nullable=False)

    subjects = relationship("Subject", back_populates="professor")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject = Column(String(150), nullable=False, unique=True)
    professor_id = Column(Integer, ForeignKey('professors.id', ondelete="CASCADE"))

    professor = relationship('Professor', back_populates='subjects')
    grades = relationship('Grade', back_populates='subject')


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    created_at = Column(Date, nullable=False)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey('students.id', ondelete="CASCADE"))

    subject = relationship('Subject', back_populates='grades')
    student = relationship('Student', back_populates='grades')