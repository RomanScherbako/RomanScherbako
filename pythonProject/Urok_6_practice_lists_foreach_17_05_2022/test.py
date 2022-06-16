matrix = [
    [1, 2, 3, 4],
    [-1, 9, 0, -2],
    [4, -2, 7, 1],
    [4, 2, 2, -9]
]

counter_first = 1

for i in matrix:
    counter_neg_number = 0
    for a in i:
        if a < 0:
            counter_neg_number += 1
    print('Количество отрицательых чисел в ', counter_first, '1-ом:', counter_neg_number)
