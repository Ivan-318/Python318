# Создать класс Student, который будет содержать имя и распечатывать информацию, а так же вложенный класс, который будет
# содержать информацию о ноутбуке с техническими характеристиками: модель, процессор и память.
# У двух однотипные ноутбуки, Roman и Vladimir - экземпляры наружного класса Student; характеристики -> внутреннего

# Roman => HP, i7, 16
# Vladimir => HP, i7, 16

class Student:
    def __init__(self, name):
        self.name = name
        self.note = self.Notebook()

    def show(self):
        print(self.name, end="")
        self.note.show()

    class Notebook:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i7"
            self.ram = 16

        def show(self):
            print(f" => {self.brand}, {self.cpu}, {self.ram}")


s1 = Student("Roman")
s2 = Student("Vladimir")

s1.show()
s2.show()
