import sqlite3
db_name = 'writing_database.db'
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

def get_id_grammar(table):
    open()
    query = f"SELECT id FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_id():
    open()
    query = f"SELECT DISTINCT id FROM writing_database ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_topic():
    open()
    query = f"SELECT DISTINCT topic FROM writing_database ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_task():
    open()
    query = f"SELECT DISTINCT task FROM writing_database ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_tips():
    open()
    query = f"SELECT DISTINCT tips FROM writing_database ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_sample():
    open()
    query = f"SELECT DISTINCT sample FROM writing_database ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_data1():
    return list(zip(get_topic(), get_task(), get_tips(), get_sample()))

print(get_data1())