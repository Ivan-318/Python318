CREATE TABLE IF NOT EXIST mainmenu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    url TEXT NOT NULL
);
--Запрос не заработал
CREATE TABLE IF NOT EXIST courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    description TEXT NOT NULL,
    time INTEGER NOT NULL
)
--Сработало это:
CREATE TABLE courses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    price INTEGER NOT NULL,
    description TEXT NOT NULL,
    time INTEGER NOT NULL
)

