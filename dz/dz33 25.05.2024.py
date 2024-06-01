# Реализовать парсинг данных из любого интернет ресурса с однотипными данными и сохранить их в формате csv.
# Ресурс https://riptutorial.com/html/example/810/hello-world.
# Получаем однотипные данные класса: class="navbar-nav" -> links.csv

import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("links.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(data)


def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    ul = soup.find("ul", class_="navbar-nav")
    links = ul.find_all("li")

    for link in links:
        url = link.find("a").get("href")
        data = [url]
        write_csv(data)


def main():
    url = "https://riptutorial.com/html/example/810/hello-world"
    html = get_html(url)
    get_data(html)


if __name__ == '__main__':
    main()
