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




