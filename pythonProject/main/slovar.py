# my_dict = {"Мяч": "150 y.e.", "Машинка": "100 y.e.", "Динозавр": "200", "Кукла": "130 у.е."}
#
# user_input = input('Введите название игрушки для отображения цены: ')
# print(my_dict[user_input])

my_dict = {1: "вы ввели единицу",
           2: "абсолютно разные значеничя",
           3: "некоторый текст",
           4: "вы ввели 4"}

while True:
    user_input = int(input('Введите число: '))
    if user_input < 5 and user_input > 0:
        print(my_dict[user_input])
        break
    else:
        print(my_dict.get(user_input, "Что то пошло не так, повторите ввод"))
        continue


