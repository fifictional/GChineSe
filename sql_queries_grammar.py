import sqlite3
db_name = 'grammar_database.db'
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

def get_difficulty(table):
    open()
    query = f"SELECT DISTINCT difficulty FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_structure(table, difficulty):
    open()
    query = f"SELECT structure FROM {table} WHERE difficulty = {difficulty}"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_structure_odr(table):
    open()
    query = f"SELECT structure FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_meaning(table):
    open()
    query = f"SELECT meaning FROM {table} ORDER BY id"
    cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result

def get_data():
    return list(zip(get_meaning("grammar_list"), get_structure_odr("grammar_list")))



print(get_data())
