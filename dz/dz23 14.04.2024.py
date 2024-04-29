# Создайте класс для подсчёта площади геометрических фигур. Класс должен предоставлять функциональность для подсчёта
# площади треугольника по разным формулам, площади прямоугольника, площади квадрата.
# Методы класса для подсчёта площади должны быть реализованы с помощью статических методов. Также класс должен считать
# количество подсчётов площади и возвращать это значение с помощью статического метода.

# Площадь треугольника по формуле Герона (3,4,5): 6.0
# Площадь треугольника через основание и высоту (6,7) : 21.0
# Площадь квадрата (7): 49
# Площадь прямоугольника (2,7): 12
# Количество подсчётов площади: 4

# class Geometry:
#     count = 0
#
#     @staticmethod
#     def triangle_area_heron(a, b, c):
#         s = (a + b + c) / 2
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#         Geometry.count += 1
#         return area
#
#     @staticmethod
#     def triangle_area_base_height(base, height):
#         area = 0.5 * base * height
#         Geometry.count += 1
#         return area
#
#     @staticmethod
#     def square_area(side):
#         area = side ** 2
#         Geometry.count += 1
#         return area
#
#     @staticmethod
#     def rectangle_area(length, width):
#         area = length * width
#         Geometry.count += 1
#         return area
#
#     @staticmethod
#     def get_count():
#         return Geometry.count
#
#
# print("*" * 60)
# print("Площадь треугольника по формуле Герона (3,4,5):", Geometry.triangle_area_heron(3, 4, 5))
# print("Площадь треугольника через основание и высоту (6,7):", Geometry.triangle_area_base_height(6, 7))
# print("Площадь квадрата (7):", Geometry.square_area(7))
# print("Площадь прямоугольника (2,7):", Geometry.rectangle_area(2, 7))
# print("Количество подсчётов площади:", Geometry.get_count())
# print("*" * 60)

# Решали в классе 21.04.2024

import math


class Area:
    count = 0

    @staticmethod
    def triangle_area_1(a, b, c):
        p = (a + b + c) / 2
        Area.count += 1
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    @staticmethod
    def triangle_area_2(a, h):
        Area.count += 1
        return 0.5 * a * h

    @staticmethod
    def square_area(a):
        Area.count += 1
        return a ** 2

    @staticmethod
    def rect_area(a, b):
        Area.count += 1
        return a * b

    @staticmethod
    def get_count():
        return Area.count


print(f"Площадь треугольника по формуле Герона: {Area.triangle_area_1(3, 4, 5)}")
print(f"Площадь треугольника через основание и высоту: {Area.triangle_area_2(6, 7)}")
print(f"Площадь квадрата: {Area.square_area(7)}")
print(f"Площадь квадрата: {Area.square_area(3)}")
print(f"Площадь квадрата: {Area.square_area(9)}")
print(f"Площадь прямоугольника: {Area.rect_area(2, 6)}")
print(f"Количество подсчётов площади: {Area.get_count()}")  # Количество подсчётов площади: 6
