user_input = input('Введите слово: ')
user_input.lower()
counter = {}
for item in user_input:
    if item in counter:
        counter[item] = counter[item] + 1
    else:
        counter[item] = 1
print(counter)
