import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('../database/university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


with open("../queries/query_1.sql", "r") as file:
    sql = file.read()


for i in execute_query(sql):
    print(i)