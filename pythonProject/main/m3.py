matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
l_1 = []

for ithem in matrix:
    sum_1 = 0
    for ithem2 in ithem:
        sum_1 = ithem2 + sum_1
    l_1.append(sum_1)
print(l_1)