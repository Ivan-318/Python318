from controller import Controller  # использует модуль, берёт из него class Controller


def main():
    app = Controller()  # создаёт экземпляр класса Controller
    app.run()  # вызывает главный метод для запуска


if __name__ == '__main__':  # если запуск идёт с этого документа,
    main()  # то вызываем метод main()
