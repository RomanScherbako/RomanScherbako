matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
matrix2 = []
const = int(input('Введите константу: '))
for ithem in matrix:
    first = []
    for ithem2 in ithem:
        first.append(ithem2 * const)
    matrix2.append(first)
for ithem2 in matrix2:
    print(ithem2)