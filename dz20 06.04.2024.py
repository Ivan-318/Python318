# Напишите программу, которая сделает сканирование выбранной директории и для всех её объектов
# выведет следующую информацию на экран: имя - тип - размер (только для файлов)

# Типы объектов: файл, директория
# Размер: только для файлов

# Пример вывода:
# project.txt - file - 658 bytes
# test - dir
# test.txt - file - 830 bytes
# test1 - dir


import os

dir_name = "nested1"  # привязываем к директории

objs = os.listdir(dir_name)
print(objs)

for obj in objs:
    p = os.path.join(dir_name, obj)
    # print(p) - полный путь
    if os.path.isfile(p):
        print(f"{obj} - file - {os.path.getsize(p)} bytes")
    elif os.path.isdir(p):
        print(f"{obj} - dir")
