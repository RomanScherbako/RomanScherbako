n = int(input())
m = int(input())
l_2 = []
for ithem2 in range(m):
    l_1 = []
    for ithem in range(n):
        number1 = int(input('Введите число: '))
        l_1.append(number1)
    l_1[0], l_1[1] = l_1[1], l_1[0]
    l_2.append(l_1)
l_2[0], l_2[1] = l_2[1], l_2[0]
print(*l_2, sep='\n')