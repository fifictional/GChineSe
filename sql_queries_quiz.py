import sqlite3
from random import *

db_name = 'vocabulary_database_quiz.db'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()



def get_question_after(table_name, question_id=1):
    open()
    query = f"SELECT question FROM {table_name} WHERE id == ? ORDER BY RANDOM()"
    cursor.execute(query, [question_id])
    result = cursor.fetchone()
    conn.commit()
    close()
    return result



def get_answers_after(table_name, answer_id=1):
    open()
    query = f"SELECT answer, wrong1, wrong2, wrong3 FROM {table_name} WHERE id == ? ORDER BY RANDOM()"
    cursor.execute(query, [answer_id])
    result = cursor.fetchone()
    conn.commit()
    close()
    return result

def check_answer(q_id, answer, table_name):
    query = f"SELECT answer FROM {table_name} WHERE id = {q_id}"
    open()
    cursor.execute(query)
    result = cursor.fetchone()
    close()
    if answer == result[0]:
        return True
    return False

def get_table_length(table_name):
    open()
    query = f"SELECT COUNT(id) FROM {table_name} WHERE id IS NOT NULL"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.commit()
    close()
    return result[0]



# print(get_question_after("cultural_life_quiz"))
# print(get_table_length("cultural_life_quiz"))
