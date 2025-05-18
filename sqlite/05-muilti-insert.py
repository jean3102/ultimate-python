import sqlite3

try:

    with sqlite3.connect("sqlite/app.db") as con:
        curso = con.cursor()
        users = [
            (2, "marcos"),
            (3, "Kanky")
        ]
        curso.executemany("INSERT INTO users values(?,?)", users)
except sqlite3.Error as e:
    print(f"Database Error: {e}")
