n = int(input('Введите число: '))
list_1 = []

def my_range_1(n):
    ind = 0
    while ind < n:
        list_1.append(ind)
        ind = ind + 1
    return list_1

a = my_range_1(n)
print(a)