a = [18, 3, -6, 81, 14, -11, 7, 21]

b = []

for n in a:

    if abs(n) > 8:

        b.append(n)

min_b = min(b)

min_b = min_b ** 2

print(min_b)
