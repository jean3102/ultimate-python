import sqlite3

try:
    with sqlite3.connect("sqlite/app.db") as con:
        cursor = con.cursor()
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchone())
except sqlite3.Error as e:
    print(f"database Error: {e}")
