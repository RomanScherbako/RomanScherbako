n = int(input())
m = int(input())

l_2 = []
l_3 = []
for ithem2 in range(m):
    l_1 = []
    for ithem in range(n):
        number1 = int(input('Введите число: '))
        l_1.append(number1)
    l_2.append(l_1)
print(*l_2, sep='\n')
