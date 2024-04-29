# Создать класс Person с двумя закрытыми свойствами: имя и возраст. С использованием декоратора @property
# создать возможность изменения этих свойств, а также возможность их удаления. Сделать дополнительные проверки,
# чтобы в поле ввода _Person__name нельзя было ввести число, а можно было ввести только тип данных str; а в поле ввода
# _Person__old можно было ввести только тип данных int. Сделать дополнительную проверку через декоратор @property, чтобы
# в случае введения некорректного типа данных в _Person__name и _Person__old он не дал этим данным записаться, в случае
# корректного ввода пусть выводит эти значения. Предусмотреть возможность удаления @deleter.

# {'_Person__name': 'Irina', '_Person__old': 26}
# Igor
# 31
# {'_Person__old': 26}

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        # if isinstance(value, str):
        #     self.__name = value
        # else:
        #     raise ValueError("Имя должно быть строкой.") Другой способ записи ->
        if not isinstance(value, str):
            raise TypeError("Имя должно быть строкой")
        else:
            self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value
        else:
            raise ValueError("Возраст должен быть целым числом.")

    @property
    def info(self):
        return f"Name: {self.name}, Age: {self.age}"

    @name.deleter
    def name(self):
        print("Удаление свойства имя")
        del self.__name

    @age.deleter
    def age(self):
        print("Удаление свойства возраст")
        del self.__age


person = Person("Irina", 26)
# print(person.info)  # Выводит: Name: Irina, Age: 26
print(person.__dict__)  # {'_Person__name': 'Irina', '_Person__age': 26}

person.name = "Igor"  # Устанавливает новое имя
person.age = 31  # Устанавливает новый возраст
# print(person.info)  # Выводит: Name: Igor, Age: 31
print(person.name)  # Igor
print(person.age)  # 31

del person.name  # Удаляет имя
del person.age  # Удаляет возраст
