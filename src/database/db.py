import sqlite3 as sql

def get_all_movies(): #Read
    conn = sql.connect("databases.db")
    cur = conn.cursor()

    rows = cur.execute("SELECT id, title, genre FROM library").fetchall()
    return rows


def add_to_db(title, genre): #Add
    conn = sql.connect("databases.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS library(id INTEGER PRIMARY KEY, title TEXT, genre TEXT)")
    cur.execute("INSERT INTO library (title, genre) VALUES (?, ?)", (title, genre))    
    conn.commit()


def remove_from_db(movie_id): #Remove
    conn = sql.connect("databases.db")
    cur = conn.cursor()
    
    cur.execute("DELETE FROM library WHERE id = ?", (movie_id,))
    conn.commit()


def get_movie(movie_id): #Read one
    conn = sql.connect("databases.db")
    cur = conn.cursor()

    row = cur.execute("SELECT id, title, genre FROM library WHERE id = ?", (movie_id,)).fetchone()
    return row


def update_in_db(movie_id, title, genre): #Update
    conn = sql.connect("databases.db")
    cur = conn.cursor()

    cur.execute("UPDATE library SET title = ?, genre = ? WHERE id = ?", (title, genre, movie_id))
    conn.commit()
