import sqlite3
conn = sqlite3.connect("app.db")

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
               id INTERGER primary key,
               name VARCHAR(50));
""")
conn.commit()
conn.close()
