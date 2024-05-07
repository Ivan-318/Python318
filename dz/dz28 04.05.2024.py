# Создать класс Shape и три дочерних класса: Square, Rectangle, Triangle.
# Родительский класс должен иметь абстрактные методы нахождения параметра, площади, рисования фигуры и вывода
# информации. С помощью полиморфизма реализуйте вывод информации о дочерних фигурах.

from math import sqrt
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def find_perimeter(self):  # нахождение периметра
        pass

    @abstractmethod
    def find_area(self):  # нахождение площади
        pass

    @abstractmethod
    def draw_shape(self):  # рисование фигуры
        pass

    @abstractmethod
    def display_info(self):  # вывод информации
        pass


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def find_area(self):
        return self.side * self.side

    def find_perimeter(self):
        return 4 * self.side

    def draw_shape(self):
        for i in range(self.side):
            print('*' * self.side)

    def display_info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.find_area()}")
        print(f"Периметр: {self.find_perimeter()}")
        print("Рисую квадрат:")
        self.draw_shape()


class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def find_area(self):
        return self.length * self.width

    def find_perimeter(self):
        return 2 * (self.length + self.width)

    def draw_shape(self):
        for i in range(self.width):
            print('*' * self.length)

    def display_info(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.find_area()}")
        print(f"Периметр: {self.find_perimeter()}")
        print("Рисую прямоугольник:")
        self.draw_shape()


class Triangle(Shape):
    def __init__(self, base, height, color):
        self.base = base
        self.height = height
        self.color = color

    def find_area(self):
        return 0.5 * self.base * self.height

    def find_perimeter(self):
        pass

    def draw_shape(self):
        for i in range(self.height):
            print(' ' * (self.height - i) + '*' * (2 * i + 1))

    def display_info(self):
        print("===Треугольник===")
        print(f"Основание: {self.base}")
        print(f"Высота: {self.height}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.find_area()}")
        print("Рисую треугольник:")
        self.draw_shape()


class HeronTriangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def find_perimeter(self):
        return (self.side1 + self.side2 + self.side3) / 2

    def find_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        s = sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))
        return round(s, 2)

    def draw_shape(self):
        for i in range(self.side2):
            print(' ' * (self.side2 - i) + '*' * (2 * i + 1))

    def display_info(self):
        print("===Треугольник по Герону===")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.find_area()}")
        print(f"Периметр: {self.find_perimeter()}")
        print("Рисую треугольник:")
        self.draw_shape()


# создаем объекты фигур
square = Square(3, "red")
rectangle = Rectangle(3, 7, "green")
triangle = Triangle(5, 7, "red")
h_triangle = HeronTriangle(11, 6, 6, "yellow")

# Полиморфизм
shapes = [square, rectangle, triangle, h_triangle]
for shape in shapes:
    shape.display_info()
