import random
print('Добро пожаловать в игру угадай число!')
secret_number = random.randint(1, 10)
print('Число загаданно')
user_number = 0
counter = 0
while counter != 4:
    user_number = int(input('Введите число ваше число: '))
    counter = counter + 1
    if counter == 4:
        print('Ваши попытки закончились! Количество попыток ', counter)
        break
    if user_number > secret_number:
        print('Загаданное число меньше')
        continue
    elif user_number < secret_number:
        print('Загаданное число больше')
        continue
    elif user_number == secret_number:
        print('Поздравляю, вы угадали. Количество попыток: ', counter)
        break



