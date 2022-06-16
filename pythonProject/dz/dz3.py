user_number = 0
counter = 0
errors = 0
l_1 = []
while counter != 10:
    while errors <= 3:
        user_number = int(input('Введите число: '))
        if user_number < 10:
            l_1.append(user_number)
            break
        elif user_number <= 0:
            continue
        elif user_number >= 10:
            continue
        errors = errors + 1
        l_1.append(user_number)
    errors = 0
    counter = counter + 1
print('Среднее арифметическое введенных чисел: ', sum(l_1) / 10)
print('Сумма всех введеных чисел пользователем: ', sum(l_1))