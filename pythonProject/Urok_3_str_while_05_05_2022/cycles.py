# Цикл с условием
# Цикл while (пока)

n = int(input())

counter = 2
while counter <= n:
    print(counter)
    counter += 2

# пользователь вводит n
# мы печатаем четные число от 0 до n

# 50
# 2
# 4

user_input = input()

# user
# u
# s
# e
# r
str_len = len(user_input)
index = 0
while index < str_len:
    print(user_input[index])
    index += 1

a = 'g'
b = 'c'

# swap двух переменных
swap = b
b = a
a = swap

a, b = b, a


# Сформировать список из введеных данных пользователем
# Добавлять данные до тех пор, пока пользователь не введет 0

# abc  input()
# 123  input()
# 456  input()
# lkj  input()
# 0

i = []
user_input = input()
while user_input != '0':
    i.append(user_input)
    user_input = input()




