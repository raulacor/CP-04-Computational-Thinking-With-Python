import sqlite3 as sql


def add_to_db(title, genre):
    conn = sql.connect("databases.db")
    cur = conn.cursor()

    #cur.execute("CREATE TABLE library(title, genre)")
    cur.execute(f"INSERT INTO library VALUES ('{title}', '{genre}')")
    conn.commit()