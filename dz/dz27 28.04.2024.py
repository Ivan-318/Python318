# Перегрузка операторов -> см в папке 27. Перегрузка операторов
class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY

    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(
            x):  # не можем обратиться за пределами класса (два подчёркивания), он и не нужен (добавлять "0" к числу)
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):  # для сложения -> перегрузка оператора для "+"
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other):  # для вычитания -> перегрузка оператора для "-"
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec - other.sec)

    def __mul__(self, other):  # для умножения -> перегрузка оператора для "*"
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec * other.sec)

    # Проверка оператора деление -> действительно возникает ошибка, т.к. получаем тип данных float
    # def __truediv__(self, other):  # для деления -> перегрузка оператора для "/"
    #     if not isinstance(other, Clock):
    #         raise ArithmeticError("Правый операнд должен быть типом Clock")
    #     return Clock(self.sec / other.sec)  # ValueError: Секунды должны быть целым числом

    def __floordiv__(self, other):  # для целочисленного деления -> перегрузка оператора для "//"
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec // other.sec)

    def __mod__(self, other):  # для остатка от деления -> перегрузка оператора для "%"
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec % other.sec)

    def __iadd__(self, other):  # для оператора +=
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.sec += other.sec
        return self

    def __isub__(self, other):  # для оператора -=
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.sec -= other.sec
        return self

    def __imul__(self, other):  # для оператора *=
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.sec *= other.sec
        return self

    def __ifloordiv__(self, other):  # для оператора /=
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.sec //= other.sec
        return self

    def __imod__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        self.sec %= other.sec
        return self

    # Сравнение
    def __eq__(self, other):  # для оператора равенство -> перегрузка оператора для "=="
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec == other.sec

    def __ne__(self, other):  # для оператора неравенство -> перегрузка оператора для "!="
        return not self.__eq__(other)
    # if not isinstance(other, Clock):  # для оператора неравенство (др. способ) -> перегрузка оператора для "!="
    #     raise ArithmeticError("Правый операнд должен быть типом Clock")
    # return self.sec != other.sec

    def __lt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec < other.sec

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return self.sec > other.sec

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


c1 = Clock(100)
c2 = Clock(200)
print(c1.get_format_time())  # 0:1:40; c __get_form(x) 00:01:40
print(c2.get_format_time())  # 00:03:20
c3 = c1 + c2  # только тип данных Clock
print(c3.get_format_time())  # 00:05:00 Проверим работу "+=" - перезапись c1:
# c1 += c2
c4 = c1 + c2 + c3  # работает за счёт __add__
print(c4.get_format_time())  # 00:10:00
c5 = c4 - c2
print(c5.get_format_time())  # 00:06:40
c6 = c5 * c1
print(c6.get_format_time())  # 11:06:40
# c7 = c6 / c2
# print(c7.get_format_time())  # ValueError: Секунды должны быть целым числом -> верно для типа данных float
# Целочисленное деление
c7 = (c6 // c5)  # 00:01:40
print(c7.get_format_time())
# Остаток от деления
c8 = c6 % c5
print(c8.get_format_time())  # 00:00:00
# Операторы присваивания:
c7 += c8
print(c7.get_format_time())  # 00:01:40
c6 -= c5
print(c6.get_format_time())  # 11:00:00
c4 *= c5
print(c4.get_format_time())  # 18:40:00
c6 //= c4
print(c6.get_format_time())  # 00:00:00
c4 %= c5
print(c4.get_format_time())  # 00:00:00

print("*" * 50)

# Равенство
if c1 == c2:
    print("Время равно")
else:
    print("Время разное")
# Неравенство
if c1 != c2:
    print("Время разное")
else:
    print("Время равно")
# Сравнение
if c1 < c2:
    print("Время меньше")
elif c1 <= c2:
    print("Время меньше или равно")

if c1 > c2:
    print("Время больше")
elif c1 >= c2:
    print("Время больше или равно")
