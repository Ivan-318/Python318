# Заполните один кортеж десятью случайными целыми числами от 0 до 5.
# Также заполните второй кортеж числами от - 5 до 0. Для заполнения кортежей числами напишите одну
# Объедините два кортежа с помощью оператора +, создав тем самым третий кортеж. С помощью метода кортежа count()
# определите в нём количество
# Выведите на экран третий кортеж и количество нулей в нём.
# import random
#
#
# def generate_tuples():
#     a = tuple(random.randint(0, 5) for _ in range(10))
#     b = tuple(random.randint(-5, 0) for _ in range(10))
#     return a, b
#
#
# a, b = generate_tuples()
# c = a + b
# count_zeros = c.count(0)
#
# print("Третий кортеж:", c)
# print("Количество нулей:", count_zeros)

# Разбор в классе:
from random import randint


def ran(a, b):
    return tuple(randint(a, b) for i in range(10))


tpl1 = ran(0, 5)
tpl2 = ran(-5, 0)
print(tpl1)
print(tpl2)
tpl3 = tpl1 + tpl2
print(tpl3)
print("0 =", tpl3.count(0))  # Подсчёт количества нулей
