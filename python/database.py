import sqlite3

#crear conexión con bd /LINKEAR CON SQLITE !!!!!
def connect():
    return sqlite3.connect("data/bazar.db")

#iniciar la base de datos/ cambiar a español acuerdate que tu papá no sabe ingles
def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL,
        stock INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY,
        date TEXT,
        total REAL
    )
    """)

    conn.commit()
    conn.close()
