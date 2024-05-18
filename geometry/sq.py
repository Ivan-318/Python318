class Square:
    def __init__(self, a):
        self.a = a

    def get_perimeter(self):
        return 4 * self.a


if __name__ == '__main__':  # чтобы код не выводился при запуске main
    print("Код в документе sq.py")
    s1 = Square(10)
    s2 = Square(20)
    print("Код в документе sq.py:", s1.get_perimeter())
    print("Код в документе sq.py:", s2.get_perimeter())
