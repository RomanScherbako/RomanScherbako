data = []
user_input = int(input('Введите кол-во запрашиваемых данных '))
j = 0
for ithem in range(user_input):
    j = int(input('Введите число '))
    if j % 2 != 0:
        data.append(j)
for cos in data:
    print(cos * 2)
