# Спарсить данные с нескольких страниц любого интернет ресурса с использованием объектно-ориентированного подхода.

from parsers import Parser


def main():
    for s in range(1, 3):
        url = f"https://www.ixbt.com/live/index/news/page{s}/"
        path = f"news_page_{s}.txt"
        pars = Parser(url, path)
        pars.run()


if __name__ == '__main__':
    main()
