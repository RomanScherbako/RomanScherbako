counter = {}
user_input = int(input('Введите число: '))
user_input = user_input + 1
for ithem in range(user_input):
    counter[ithem] = ithem ** 2
print(counter)


