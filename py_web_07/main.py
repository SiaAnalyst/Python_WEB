import sys
import os
from datetime import datetime
import argparse
import sqlalchemy
from sqlalchemy.sql import select, update, insert, delete

sys.path.append(os.getcwd())

from database.models import Group, Student, Professor, Subject, Grade
from database.db_connect import conn

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action", choices=['create', 'list', 'update', 'remove'], required=True)
parser.add_argument("-m", "--model", choices=['Group', 'Student', 'Professor', 'Subject', 'Grade'], required=True)
parser.add_argument("-id", "--id", type=int, default=None)
parser.add_argument("-n", "--name", type=str, default=None)
parser.add_argument("-fn", "--fullname", type=str, default=None)
parser.add_argument("-ci", "--group_id", type=int, default=None)
parser.add_argument("-ti", "--professor_id", type=int, default=None)
parser.add_argument("-sui", "--subject_id", type=int, default=None)
parser.add_argument("-si", "--student_id", type=int, default=None)
parser.add_argument("-g", "--grade", type=int, default=None)
parser.add_argument("-d", "--created_at", type=str, default=None)

args = parser.parse_args()


def execute_query(args):
    if args.action == "list":
        query = eval(f"select({args.model})")

    elif args.action == "create":
        model = args.model
        if model == "Group":
            values = f"group_name='{args.name}'"
        elif model == "Student":
            values = f"student='{args.fullname}', group_id={args.group_id}"
        elif model == "Professor":
            values = f"professor='{args.fullname}'"
        elif model == "Subject":
            values = f"subject='{args.name}', professor_id={args.professor_id}"
        elif model == "Grade":
            values = f"grade={args.grade}, created_at=datetime.strptime('{args.created_at}', '%Y-%M-%d').date(), student_id={args.student_id}, subject_id={args.subject_id}"
        query = eval(f"insert({args.model}).values({values})")

    elif args.action == "update":
        model = args.model
        if model == "Group":
            values = f"group_name='{args.name}'"
        elif model == "Student":
            values = f"student='{args.fullname}'"
        elif model == "Professor":
            values = f"professor='{args.fullname}'"
        elif model == "Subject":
            values = f"subject='{args.fullname}'"
        elif model == "Grade":
            values = f"grade={args.grade}"

        query = eval(f"update({args.model}).values({values}).where(eval(f'{args.model}.id=={args.id}'))")

    elif args.action == "remove":
        query = eval(f"delete({args.model}).where(eval(f'{args.model}.id=={args.id}'))")

    return conn.execute(query)


if __name__ == '__main__':
    for r in execute_query(args):
        print(r)