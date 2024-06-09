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

import sqlite3

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


with sqlite3.connect("db_3.db") as con:
    cur = con.cursor()

    cur.execute("""
    SELECT *
    FROM T1
    LIMIT 2, 5
    """)

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

    res3 = cur.fetchall()
    print(res3)  # [(6, 'Васильев', 'Менеджер', 6, 1750.0), (7, 'Дзюба', 'Переводчик', 2, 1380.0)]
    # Без res и res2 [(3, 'Бутенко', 'Директор', 7, 2560.0), (4, 'Бутков', 'Менеджер', 2, 1200.0), (5, 'Василенко',
    # 'Оператор', 6, 970.0), (6, 'Васильев', 'Менеджер', 6, 1750.0), (7, 'Дзюба', 'Переводчик', 2, 1380.0)]
