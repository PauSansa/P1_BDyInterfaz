import sqlite3
import pprint

def anadir_usuario(usuario, contrasena):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = f"INSERT INTO users(username, password) VALUES('{usuario}','{contrasena}')"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def quitar_usuario(usuario):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    query = f"DELETE FROM users WHERE username = '{usuario}'"
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def return_listas():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    return rows





return_listas()