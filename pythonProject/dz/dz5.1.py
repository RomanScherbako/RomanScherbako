print('Добро пожаловать в магазин!\nЦена на товары:\nЕлка - 200 у.е.\nГирлянда - 50 у.е.'
      '\nНовогодний венок - 25 у.е.\nНабор конфет - 30 у.е.')
pay = [200, 50,  25, 30]
user_sum = []
user_nds = []
while True:
    nixit = int(input('Начать покупки?\nДа - 1\nНет, закрыть смену - 0:\n'))
    if nixit == 0:
        print('Общая выручка: ', int(sum(user_sum)), 'у.е.')
        print('Общая сумма НДС 12%: ', int(sum(user_nds)), 'у.е.')
        break
    elif nixit == 1:
        while True:
            user_input = int(input('Выбрете товар из списка:\n0 - Елка\n1 - Гирлянда\n2 - Новогодний венок'
                               '\n3 - Нобор конфет\nДля выхода введите 5:\n'))
            if user_input == 5:
                print('Спасибо за покупки, общая сумма: ', sum(user_sum), 'у.е.')
                print('Cумма НДС 12%: ', sum(user_nds), 'у.е.')
                break
            elif user_input <= 3:
                sum_ = 0
                nds = 0
                sum_white = 0
                k = int(input('Выберите количество товара:\n'))
                sum_white = pay[user_input] * k
                nds = (sum_white * 0.12)
                sum_ = sum_white - nds
                user_sum.append(sum_)
                user_nds.append(nds)
            elif user_input > 3:
                print('Вы ввели неверное значение, повторите ввод!')
                continue


