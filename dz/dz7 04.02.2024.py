# Вычисление площади фигур, решать без функций

# Выбор фигуры:
# 1 - треугольник
# 2 - прямоугольник
# 3 - круг
# Выберете фигуру: 1
# Введите сторону a = 15
# Введите сторону b = 20
# Введите сторону c = 6
# 28.59

from math import pi
figure = int(input("Выбор фигуры:\n1 - треугольник\n2 - прямоугольник\n3 - круг\nВыберете фигуру цифрой: "))
# Вычисление площади в зависимости от выбранной фигуры
if figure == 1:
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    c = float(input("Введите сторону c: "))
    # Расчет площади треугольника
    p = (a + b + c) / 2
    fig_area = round((p * (p - a) * (p - b) * (p - c)) ** 0.5, 2)
    print(fig_area)
elif figure == 2:
    a = float(input("Введите сторону a: "))
    b = float(input("Введите сторону b: "))
    # Расчет площади прямоугольника
    fig_area = round(a * b, 2)
    print(fig_area)
elif figure == 3:
    r = float(input("Введите радиус r: "))
    # Расчет площади круга
    fig_area = round(pi * (r ** 2), 2)
    print(fig_area)
else:
    print("Ошибка: некорректный выбор фигуры")

