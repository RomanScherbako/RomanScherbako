n = int(input())
m = int(input())
l_2 = []
min = 0
max = 0
for ithem2 in range(m):
    l_1 = []
    for ithem in range(n):
        number1 = int(input('Введите число: '))
        l_1.append(number1)
    l_2.append(l_1)
for ithem in l_2:
    for ithem2 in ithem:
        if min < ithem2:
            min = ithem2
        elif max > ithem2:
            max = ithem2
if min > max:
    l_2[0], l_2[1] = l_2[1], l_2[0]
print(*l_2, sep='\n')