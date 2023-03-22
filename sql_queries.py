import sqlite3
db_name = 'vocabulary_database.db'
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
    data = cursor.fetchall()
    print(data)
    conn.commit()


def get_id(table):
    open()
    query = f"SELECT id FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result


def get_chinese(table):
    open()
    query = f"SELECT chinese FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_english(table):
    open()
    query = f"SELECT english FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result



