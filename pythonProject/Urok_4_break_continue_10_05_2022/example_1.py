# Пользователь вводит числа
# До тех пор пока не введет 0
# Вывести на экран сумму всех
# чисел введенных пользователем

# Пример ввода:
# 4
# 5
# 5
# 8
# 2
# 1
# 0

# Вывод:
# 25

# while True:
#   ...
#
# b = 0
# while True:
#     a = int(input())
#     if a == 0:
#         break
#     b += a
# print(b)

# a = int(input())
# b = 0
# while a != 0:
#     b += a
#     a = int(input())
# print(b)

# b = 0
# while (a := int(input())) != 0:
#     b += a
# print(b)

sum_ = 0
while True:
    user_number = int(input())
    if user_number == 0:
        break
    sum_ += user_number
print(sum_)

sum_ = 0
while True:
    if (user_number := int(input())) == 0:
        break
    sum_ += user_number
print(sum_)

sum_ = 0
while True:
    user_number = int(input())
    if user_number != 0:
        sum_ += user_number
    else:
        break
print(sum_)
