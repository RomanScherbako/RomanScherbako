counter = []
while True:
    user_input = input('Введите число: ')
    if len(user_input) == 0:
        break
    else:
        counter.append(int(user_input))
def my_sum(counter):
    return sum(counter)
print('Сумма всех элементов равна: ', my_sum(counter))

