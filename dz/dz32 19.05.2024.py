# Преобразовать 200 todos json в csv по ссылке https://jsonplaceholder.typicode.com/todos,
# сохранить их в документе todos.csv. Данные для todos.csv получить по ссылке:
# https://jsonplaceholder.typicode.com/todos
# response = requests.get("https://jsonplaceholder.typicode.com/todos") -

import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos")  # строка для отправки GET запроса на указанный
# URL адрес и получения данных в формате JSON

# Посмотреть полученные данные
# print(response.text)

# Сохраняю данные в переменную

todos = json.loads(response.text)
print(todos)

# # Выводим данные в формате JSON
# print(response.json())

with open("response.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(todos[0].keys()))
    writer.writeheader()
    for t in todos:
        writer.writerow(t)  # получил response.csv ++
