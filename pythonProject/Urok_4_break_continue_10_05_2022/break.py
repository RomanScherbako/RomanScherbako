...

# С помощью цикла while
# Вывести на экран нечетные числа от 1 до 5

# 1
# 2
# 3
# 4
# 5

# counter (счетчик)

# counter = 10
# limit = 0
# step = -2
#
# while counter >= limit:  # hardcode
#     print(counter)
#     counter += step

# counter = 1
# while counter <= 5:
#     print(counter)
#     counter += 1

counter = 1
while True:
    if counter > 5:
        break  # Оператор break
    print(counter)
    counter += 1

print("Цикл завершился")

while True:
    print("Бесконечный цикл запущен")
    break
