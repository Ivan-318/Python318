# Занятие 35. 26.05.2024. Функциональный подход
# import csv
#
# # Парсинг. Ресурс: https://ru.wordpress.org/plugins/ <- получить 24 стр на каждой по 20 плагинов!
# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("div", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3", class_="entry-title").text
#         except AttributeError:
#             name = ""
#
#         try:
#             # url = el.find("h3", class_="entry-title").find('a').get("href") # 1 способ
#             url = el.find("h3", class_="entry-title").find('a')["href"]  # 2 способ
#         except AttributeError:
#             url = ""
#         # print(name)
#         # print(url)
#
#         try:
#             active = el.find("span", class_="active-installs").text.strip()  # strip() - убирает межстрочные отступы
#         except AttributeError:
#             active = ""
#         # print(active)  # получили активные установки
#
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except AttributeError:
#             # c = ""
#             cy = ""
#         # print(c)
#
#         data = {
#             'name': name,
#             'url': url,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#         # print(cy)
#         # print(data)
#
#
# def main():
#     for i in range(2, 25):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"  # получили 300 записей в plugins1.csv
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# Парсинг ООП -> parsers.py

# from parsers import Parser
#
#
# def main3():
#     pars = Parser("https://www.ixbt.com/live/index/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main3()

# Шаблоны проектирования. Модель MVC
# Задача. Создать приложение, которое позволит манипулировать статьями. Необходимо хранить информацию:
# - название статьи
# - автор статьи
# - количество страниц
# - краткое описание.
# Создайте классы и методы для этого приложения. Реализуйте паттерн MVC.

# Занятие 37. 02.06.2024. СУБД.

# import sqlite3

# Первый способ создания БД
# con = sqlite3.connect("profile.db")  # соединение с БД
# cur = con.cursor()  # соединение с объектом курсора
#
# cur.execute(""" # запросы
# """)
#
# con.close()  # закрыть БД, обязательно!

# Второй способ создания БД. Контекстный менеджер

# # with sqlite3.connect("profile.db") as con:
# #     cur = con.cursor()
#
#     # cur.execute("""CREATE TABLE IF NOT EXISTS USERS(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # date BLOB)""") # закрывается табуляцией автоматически
#
#     '''Удаление таблицы'''
#     # cur.execute("DROP TABLE users")

# Занятие 38. 08.06.2024. Запросы


# with sqlite3.connect("users.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT "+79090000000",
#     age INTEGER CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )""")
#
#     # Работа с созданной таблицей. 1. Переименовать таблицу
#     cur.execute("""
#     ALTER TABLE person
#     RENAME TO person_table
#     """)
#
#     # 2. Добавить поле(столбец) в таблицу
#     cur.execute("""
#        ALTER TABLE person_table
#        ADD COLUMN address NOT NULL DEFAULT "Москва"
#        """)
#
#     # 3. Удалить столбец(поле)
#     cur.execute("""
#        ALTER TABLE person_table
#        DROP COLUMN address
#        """)
#
#     # 4. Переименовать существующий столбец(поле)
#     cur.execute("""
#        ALTER TABLE person_table
#        RENAME COLUMN address TO home_address
#        """)
#
#     # 5. Удаление таблицы
#     cur.execute("""
#        DROP TABLE person_table
#        """)


# with sqlite3.connect("db_3.db") as con:
#     cur = con.cursor()
#
#     cur.execute("""
#     SELECT *
#     FROM T1
#     LIMIT 2, 5
#     """)

# print(cur)  # <sqlite3.Cursor object at 0x00000170C79CAF80>
# for i in cur:
#     print(i)
# Получить данные из объекта cur

# res = cur.fetchone()
# print(res)  # (3, 'Бутенко', 'Директор', 7, 2560.0)
#
# # res2 = cur.fetchmany()
# res2 = cur.fetchmany(2)  # [(4, 'Бутков', 'Менеджер', 2, 1200.0), (5, 'Василенко', 'Оператор', 6, 970.0)]
# print(res2)  # [(4, 'Бутков', 'Менеджер', 2, 1200.0)]

# res3 = cur.fetchall()
# print(res3)  # [(6, 'Васильев', 'Менеджер', 6, 1750.0), (7, 'Дзюба', 'Переводчик', 2, 1380.0)]
# Без res и res2 [(3, 'Бутенко', 'Директор', 7, 2560.0), (4, 'Бутков', 'Менеджер', 2, 1200.0), (5, 'Василенко',
# 'Оператор', 6, 970.0), (6, 'Васильев', 'Менеджер', 6, 1750.0), (7, 'Дзюба', 'Переводчик', 2, 1380.0)]

# Занятие 40 15.06.2024
# import sqlite3
#
# cars_list = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 36000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
# # удаление марок автомобилей, начинающихся с буквы B
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)

# способ 2 без цикла

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_list)

# способ, 1 c циклом
# for car in cars_list:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit - контрольная точка
# con.close - закрыть - не используются в контекстном менеджере with

# import sqlite3
#
# con = None
# try:
#     con = sqlite3.connect("car.db")
#     cur = con.cursor()
#     cur.executescript("""
#      CREATE TABLE IF NOT EXISTS cars(
#          car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#          model TEXT,
#          price INTEGER
#      );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'Renault', 22000);
#     UPDATE cars2 SET Price = price + 100;
#      """)
#     con.commit()
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()


# Занятие 41 16.06.2024

# import sqlite3
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row    # чтобы обращаться к элементам по ключам и значениям
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)

# cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")  # см. схема данных_1
# last_row_id = cur.lastrowid
# buy_car_id = 2
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# Получим данные
# cur.execute("SELECT model, price FROM cars")

# rows = cur.fetchone()
# print(rows)  # ('Renault', 22200)
#
# rows1 = cur.fetchmany()
# print(rows1)    # [('Volvo', 29200)]
#
# rows2 = cur.fetchmany(5)
# print(rows2)    # [('Mercedes', 57200), ('Audi', 52200), ('Chevrolet', 46200), ('Daewoo', 36200),
# # ('Citroen', 29200)] - след. 5 авто

# rows3 = cur.fetchall()
# print(rows3)     # [('Honda', 33200), ('Chevrolet', 46200), ('Daewoo', 36200), ('Citroen', 29200), ('Honda', 33200),
# # ('Renault', 22100), ('Запорожец', 1000)] -> все оставшиеся элементы

# for res in cur:
#     # print(res[0], "->", res[1])
#     print(res["model"], "->", res["price"])     # далее см. схема данных_2


# import sqlite3
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     )""")
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))
#
#     cur.execute("SELECT ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava("out.png", img)

# Восстановление БД
# import sqlite3

# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "w") as f:
#         for sql in con.iterdump():
#             f.write(sql)

# with sqlite3.connect("car_project.db") as con:
#     cur = con.cursor()
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)

# ORM (Object-Relation Mapping) - реляционное сопоставление объектов
# SQLAlchemy ORM - позволяет создавать таблицы в БД через создание классов, упрощённый вариант создания SQL запросов

# import os
#
# from sqlalchemy import and_, or_, not_, desc, func
#
# from models.database import DATABASE_NAME, Session
# import create_database as db_creator
#
# from models.lesson import Lesson, association_table
# from models.student import Student
# from models.group import Group
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()
#
#     session = Session()
#     # print(session.query(Lesson).all())
#     # print("*" * 60)  # Все данные с lesson
#     #
#     # # способ 2
#     # for it in session.query(Lesson):
#     #     print(it)  # вывод в столбик
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson):
#     #     print(it.lesson_title)  # только названия уроков
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).count())  # 7
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).first())  # Предмет (ID: 1, Название: Математика) - 1й эл-мент
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(Lesson.id >= 3):  # c 3й дисциплины вывод
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(Lesson.id >= 3, Lesson.lesson_title.like('Ф%')):
#     #     print(it.lesson_title)  # "," - лог И
#     # print("*" * 60)  # Философия, Физика
#     #
#     # for it in session.query(Lesson).filter(and_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)  # корректная запись
#     #
#     # for it in session.query(Lesson).filter(or_(Lesson.id >= 3, Lesson.lesson_title.like('Ф%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)  # выводит ысе элементы ИЛИ id>3 ИЛИ с буквы "Ф"
#     #
#     # for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('М%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title is None).all())
#     # print("*" * 60)  # []
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title is not None).all())
#     # print("*" * 60)  # весь список
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title.in_(['Математика', 'Линейная алгебра'])).all())
#     # print("*" * 60)  # [Предмет (ID: 1, Название: Математика), Предмет (ID: 5, Название: Линейная алгебра)]
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title.not_in(['Математика', 'Линейная алгебра'])).all())
#     # print("*" * 60)  # всё кроме Математика и Линейная алгебра
#     #
#     # print(session.query(Lesson).filter(Lesson.lesson_title.notin_(['Математика', 'Линейная алгебра'])).all())
#     # print("*" * 60)  # Тоже, что и выше -> др. форма записи
#     #
#     # print(session.query(Student).filter(Student.age.between(16, 17)).all())  # все студенты 16-17 лет
#     # print("*" * 60)
#     #
#     # print(session.query(Student).filter(not_(Student.age.between(16, 17))).all())  # все студенты НЕ 16-17 лет
#     # print("*" * 60)
#     #
#     # print(session.query(Student).filter(not_(Student.age.between(17, 24))).all())  # все студенты НЕ 17-24 лет
#     # print("*" * 60)
#     #
#     # for it in session.query(Lesson).filter(not_(Lesson.id >= 3), not_(Lesson.lesson_title.like('М%'))):
#     #     print(it.lesson_title)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).filter(Student.age.like("1%")).limit(4):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).filter(Student.age.like("1%")).limit(4).offset(3):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).order_by(Student.surname):
#     #     print(it)
#     # print("*" * 60)  # сортировка по алфавиту фамилий
#     #
#     # for it in session.query(Student).order_by(desc(Student.surname)):
#     #     print(it)
#     # print("*" * 60)  # реверсивная сортировка по алфавиту -> о убыванию
#     #
#     # #   Выведем студентов, которые учатся в одной из заданных групп
#     #
#     # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-7'):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student).join(Group).filter(Group.group_name == 'MDA-9'):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(Group.group_name):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(func.count(Student.surname), Group.group_name).join(Group).group_by(
#     #         Group.group_name).having(func.count(Student.surname) < 25):
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student.age).distinct():    # возрасты без повторений
#     #     print(it)
#     # print("*" * 60)
#     #
#     # for it in session.query(Student.age).filter(Student.age < 20).distinct():    # с условием
#     #     print(it)
#     # print("*" * 60)
#
#     # for it in session.query(Lesson):
#     #     print(it)
#     # print("*" * 60)
#     # # Заменим одну дисциплину на другую Математика -> Информатика:
#     #
#     # i = session.query(Lesson).first()
#     # i.lesson_title = "Информатика"
#     # session.add(i)
#     # session.commit()
#
#     for it in session.query(Lesson):
#         print(it)
#     print("*" * 60)
#
#     # Добавить в таблицу
#     # session.add(Lesson(lesson_title="Математика"))
#     # session.commit()
#
#     # Удалить запись
#
#     i = session.query(Lesson).filter(Lesson.lesson_title == "Математика").first()
#     session.delete(i)
#     session.commit()
#
#     for it in session.query(Lesson):
#         print(it)
#     print("*" * 60)

# Шаблонизатор (Jinja) -> позволяет выводить данные в браузер

# from jinja2 import Template


# # name = "Игорь"
# # age = 25
# per = {'name': "Игорь", 'age': 25}
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.name }}.")
# # msg = tm.render(n=name, a=age)
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person("Игорь", 25)
#
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.get_name() }}.")
# msg = tm.render(p=per)
#
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Сочи'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ярославль'},
#     {'id': 5, 'city': 'Смоленск'},
# ]
#
# link = """<select name="cities">
#     {% for c in cities -%}
#         {% if c.id > 3 -%}
#             <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#         {% elif c.city == "Москва" %}
#             <option>{{ c['city'] }}</option>
#         {% else -%}
#             {{ c['city'] }}
#         {% endif -%}
#     {%- endfor -%}
# </select>"""
#
# tm = Template(link)
# msg = tm.render(cities=cities)
#
# print(msg)

# Занятие 43 23.06.2024

# cars = [9, 5, 6, 7, 1, 3, 8, 4, 6, 2]

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# # tpl = "Сумма: {{ cs | sum }}"
# # tpl = "Сумма: {{ cs | sum(attribute = 'price') }}"   # Сумма: 105900
# # tpl = "Максимальное: {{ cs | max(attribute = 'price') }}"   # Максимальное: {'model': 'Renault', 'price': 44300}
# # tpl = "Максимальное: {{ (cs | max(attribute = 'price')).model }}"   # Максимальное: Renault
# # tpl = "Минимальное: {{ (cs | min(attribute = 'price')).model }}"   # Минимальное: Skoda
# # tpl = "{{ cs | random }}"   # случайный эл-нт из списка
# tpl = "{{ cs | replace('model', 'brand') }}"   # model -> brand, исходная переменная cars без изменений
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
#
# print(msg)

# Макроопределение - аналог функций в шаблонизаторе

# html = """
# {% macro input_func(name, value, type="text", size=40) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}">
# {% endmacro %}
#
# <p>{{ input_func('name', 'Введите имя') }}</p>
# <p>{{ input_func('psw', 'Пароль', 'password') }}</p>
# <p>{{ input_func('email', 'Электронная почта', 'email') }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
#
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
#
# tm = env.get_template('about.html')
# msg = tm.render(users=persons, title="About Jinja")
#
# print(msg)

