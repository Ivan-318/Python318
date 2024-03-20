# Написать функцию, вычисляющую площадь прямоугольного параллелепипеда с рёбрами a, b, c. Данная функция должна
# содержать внутри себя ещё одну функцию, вычисляющую площадь прямоугольника. Решить задачу для случаев, когда общая
# площадь определена как глобальная и как локальная переменная. Внести изменения в функции таким образом,
# чтобы общая площадь могла использоваться как нелокальная переменная.

# Тестовые значения:
# 2, 4, 6
# 5, 8, 2
# 1, 6, 8

# 88
# 132
# 124

# 1-й случай. Общая площадь определена как локальная переменная
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))  # 88
# print(outer(5, 8, 2))  # 132
# print(outer(1, 6, 8))  # 124

# 2-й случай. Общая площадь определена как глобальная переменная

# Переделать в глобальную -> s - глобальная переменная

# s = 0
#
#
# def inner(i, j):
#     return i * j
#
#
# def outer(a, b, c):
#     global s
#     # Функции содержащие площади прямоугольников
#     # rectangle_s = inner(a, b)
#     # side_s = inner(b, c)
#     # top_s = inner(a, c)
#     # s = 2 * rectangle_s + 2 * side_s + 2 * top_s
#     # return s
#     # Функция, вычисляющую площадь прямоугольника
#     s = 2 * (inner(a, b) + inner(b, c) + inner(a, c))
#     return s
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)

# 2.1-й случай. Разбор в классе. S - глобальная переменная
# s = 0
#
#
# def outer(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     global s
#     s = 2 * (inner(a, b) + inner(b, c) + inner(a, c))
#     return s
#
#
# outer(2, 4, 6)
# print(s)
# outer(5, 8, 2)
# print(s)
# outer(1, 6, 8)
# print(s)

# # 3-й случай. Общая площадь определена как нелокальная переменная, метод nonlocal

# def outer(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(outer(2, 4, 6))  # 88
# print(outer(5, 8, 2))  # 132
# print(outer(1, 6, 8))  # 124

# 3.1-й случай. Разбор в классе, метод nonlocal.

def outer(a, b, c):
    s = 0

    def inner(i, j):
        nonlocal s
        s += i * j

    inner(a, b)
    inner(a, c)
    inner(b, c)
    return 2 * s


print(outer(2, 4, 6))  # 88
print(outer(5, 8, 2))  # 132
print(outer(1, 6, 8))  # 124
