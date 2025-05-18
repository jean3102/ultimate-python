import sqlite3

with sqlite3.connect("app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
            id INTERGER primary key, 
            name VARCHAR(50)
        )
    """
    )
