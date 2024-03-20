# Написать программу, которая случайным образом заполняет двумерный список размерностью 4x3 цифрами от -20 до 10.
# Необходимо найти количество отрицательных элементов.

# -18  4   -7
# -20  9   -3
# -18  -14  1
# 4   -8   -8

# Количество отрицательных элементов: 8

import random
w, h = 3, 4
matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
for row in matrix:
    for x in row:
        print(x, end="\t\t")
    print()
count = 0
for y in range(h):
    for x in range(w):
        if matrix[y][x] < 0:
            count += 1
print("\nКоличество отрицательных элементов:", count)

