n = int(input('Введите число: '))
list_1 = []
step = int(input('Введите шаг: '))
def my_range_1(n, step):
    ind = 0
    while ind < n:
        list_1.append(ind)
        ind = ind + step
    return list_1

a = my_range_1(n, step)
print(a)