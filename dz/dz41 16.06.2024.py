# Создать программно любую базу данных, в ней таблицу. Таблицу наполнить данными с помощью методов модуля sqlite3.

import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Charlie', 35)")
cursor.execute("insert into users (name, age) VALUES ('David', 40)")
cursor.execute("insert into users (name, age) VALUES ('Emily', 22)")

conn.commit()

conn.close()
