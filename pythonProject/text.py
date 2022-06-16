# number = int(input('Введите число '))
# counter = 0
# while counter < number:
#     a = int(input('Введите еще одно число '))
#     if a % 2 == 0:
#         print('Число четное!')
#     else:
#         print('Число не четное!')
#     counter = counter + 1

str_ = input('Ввведите что нибудь ')
index = 0
b = 0
while index < len(str_):
    a = int(str_[index])
    b = a + b
    index = index + 1
print(b)