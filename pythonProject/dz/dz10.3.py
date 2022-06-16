counter = []
negative = (bool(input('Добавлять в сумму отрицательные числа? Если нет, то оставьте поле ввода пустое: ')))
while True:
    user_input = input('Введите число: ')
    if len(user_input) == 0:
        break
    else:
        counter.append(int(user_input))
def my_sum(counter, negative):
    if negative == False:
        for item in reversed(range(len(counter))):
            if counter[item] < 0:
                del counter[item]
        return sum(counter)
    return sum(counter)
print('Сумма всех элементов равна: ', my_sum(counter, negative))