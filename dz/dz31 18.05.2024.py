# Задача. Есть некоторый словарь, который хранит название стран и столиц.
# Название стран используется в качестве ключа, название столицы в качестве значения.
# Необходимо реализовать: добавление, удаление, поиск, редактирование и просмотр данных
# (используя упаковку и распаковку данных)

import json

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def add_country(filename):
        country_name = input("Введите название страны: ")
        capital_name = input("Введите название столицы: ")

        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = {}

        data[country_name] = capital_name

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def delete_country(filename, country_name):
        try:
            data = json.load(open(filename))
            if country_name in data:
                del data[country_name]
                with open(filename, "w") as f:
                    json.dump(data, f, indent=2)
            else:
                print("Страны с таким названием нет в списке.")
        except FileNotFoundError:
            print("Файл не найден.")

    @staticmethod
    def search_country(filename, country_name):
        try:
            data = json.load(open(filename))
            if country_name in data:
                print(f"Страна: {country_name}, Столица: {data[country_name]}")
            else:
                print("Страны с таким названием нет в списке.")
        except FileNotFoundError:
            print("Файл не найден.")

    @staticmethod
    def edit_country(filename, country_name, new_capital):
        try:
            data = json.load(open(filename))
            if country_name in data:
                data[country_name] = new_capital
                with open(filename, "w") as f:
                    json.dump(data, f, indent=2)
            else:
                print("Страны с таким названием нет в списке.")
        except FileNotFoundError:
            print("Файл не найден.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            print(json.load(f))


file = 'list_capital.json'
index = ''
while index != '6':
    index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных"
                  "\n4 - редактирование данных\n5 - просмотр данных\n6 - завершение работы\nВведите: ")
    if index == "1":
        CountryCapital.add_country(file)
    elif index == "2":
        country_name = input("Введите название страны для удаления: ")
        CountryCapital.delete_country(file, country_name)
    elif index == "3":
        country_name = input("Введите название страны для поиска: ")
        CountryCapital.search_country(file, country_name)
    elif index == "4":
        country_name = input("Введите название страны для редактирования: ")
        new_capital = input("Введите новое название столицы: ")
        CountryCapital.edit_country(file, country_name, new_capital)
    elif index == "5":
        CountryCapital.load_from_file(file)
