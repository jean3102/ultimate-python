import sqlite3

try:
    with sqlite3.connect("sqlite/app.db") as con:
        cursor = con.cursor()
        cursor.execute("INSERT INTO users VALUES(?,?)", (1, "jean"))
except sqlite3.Error as e:
    print(f"Database error:  {e}")
