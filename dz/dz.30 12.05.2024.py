import json
from random import choice
# Нужно получить объект в объекте в формате json


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        "tel": tel
    }
    return person, tel


def write_json(person_dz_dict, num):
    try:
        data = json.load(open('persons_dz.json'))
    except FileNotFoundError:
        data = {}  # {}

    data[num] = person_dz_dict
    with open('persons_dz.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])
