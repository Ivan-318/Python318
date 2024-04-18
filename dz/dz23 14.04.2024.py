# Создайте класс для подсчёта площади геометрических фигур. Класс должен предоставлять функциональность для подсчёта
# площади треугольника по разным формулам, площади прямоугольника, площади квадрата.
# Методы класса для подсчёта площади должны быть реализованы с помощью статических методов. Также класс должен считать
# количество подсчётов площади и возвращать это значение с помощью статического метода.

# Площадь треугольника по формуле Герона (3,4,5): 6.0
# Площадь треугольника через основание и высоту (6,7) : 21.0
# Площадь квадрата (7): 49
# Площадь прямоугольника (2,7): 12
# Количество подсчётов площади: 4

class Geometry:
    count = 0

    @staticmethod
    def triangle_area_heron(a, b, c):
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        Geometry.count += 1
        return area

    @staticmethod
    def triangle_area_base_height(base, height):
        area = 0.5 * base * height
        Geometry.count += 1
        return area

    @staticmethod
    def square_area(side):
        area = side ** 2
        Geometry.count += 1
        return area

    @staticmethod
    def rectangle_area(length, width):
        area = length * width
        Geometry.count += 1
        return area

    @staticmethod
    def get_count():
        return Geometry.count


print("*" * 60)
print("Площадь треугольника по формуле Герона (3,4,5):", Geometry.triangle_area_heron(3, 4, 5))
print("Площадь треугольника через основание и высоту (6,7):", Geometry.triangle_area_base_height(6, 7))
print("Площадь квадрата (7):", Geometry.square_area(7))
print("Площадь прямоугольника (2,7):", Geometry.rectangle_area(2, 7))
print("Количество подсчётов площади:", Geometry.get_count())
print("*" * 60)
