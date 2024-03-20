# Дан словарь {'emp1': {'name': 'John', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},
# 'emp3': {'name': 'Brad', 'salary': 6500}}. Измените значение зарплаты Брэда с 6500 до 8500.

employees = {
    "emp1": {"name": 'John', "salary": 7500},
    "emp2": {"name": 'Emma', "salary": 8000},
    "emp3": {"name": 'Brad', "salary": 6500},
}
print(employees)
employees["emp3"]["salary"] = 8500

for x in employees:
    print(x)
    for y in employees[x]:
        print("\t", y, ":", employees[x][y])
