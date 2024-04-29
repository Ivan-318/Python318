# Сделать защиту, чтобы прямоугольник существовал.
# Прямоугольник green. Площадь -200.
# Сделать проверку, чтобы значения ширины и высоты не были отрицательным числом. Проверка в классе Rectangle ->
# написать if в set(проверка) <- их добавить

class Figure:
    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c


class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError(f"Значение ширины {value} должно быть положительным числом")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError(f"Значение высоты {value} должно быть положительным числом")
        self.__height = value

    def area(self):
        print(f"Прямоугольник {self.color}. Площадь: ", end="")
        return self.__width * self.__height


rect = Rectangle(10, -20, "green")
print(rect.area())
# Готово

