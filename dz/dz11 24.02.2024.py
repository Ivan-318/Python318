# Напишите функцию, которая принимает произвольное количество аргументов и возвращает словарь, в котором каждый элемент
# списка является и ключом и значением.

# {1: 1, 2: 2, 3: 3, 4: 4}
# {'grey': 'grey', (2, 17): (2, 17), 3.11: 3.11, -4: -4}

def create_dict(*args):
    result_dict = {}
    for i in args:
        result_dict[i] = i
    return result_dict


print(create_dict(1, 2, 3, 4))
print(create_dict('grey', (2, 17), 3.11, -4))
