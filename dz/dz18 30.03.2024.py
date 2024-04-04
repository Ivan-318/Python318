# Вычислить количество отрицательных чисел в массиве с использованием рекурсии в списке любой длины:
# [-2, 3, 8, -11, -4, 6]
# n = 3

def count_neg_numbers(arr1):
    count = 0
    if len(arr1) == 0:  # базовый случай
        return 0
    if arr1[0] < 0:
        count += 1
    return count + count_neg_numbers(arr1[1:])


arr = [-2, 3, 8, -11, -4, 6]
print("Количество отрицательных чисел в массиве: n =", count_neg_numbers(arr))