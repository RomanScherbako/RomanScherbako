from_ = int(input('Введите от какого числа: '))
list_1 = []
to = int(input('Введите до какого числа'))
def my_range_1(from_, to, step=1):
    while from_ < to:
        list_1.append(from_)
        from_ = from_ + step
    return list_1

a = my_range_1(from_, to, step=1)
print(a)