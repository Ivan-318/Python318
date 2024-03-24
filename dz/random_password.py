# Генератор паролей из символов ASCII на любое кол-во символов

from random import randint

min_ascii = 33
max_ascii = 126


def random_password():
    res = ""
    for i in range(8):  # 8 символов, можно и больше
        res += chr(randint(min_ascii, max_ascii))
    return res


print("Ваш случайный пароль:", random_password())