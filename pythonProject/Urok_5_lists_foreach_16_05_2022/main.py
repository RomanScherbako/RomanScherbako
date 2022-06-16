data = [
    "1", 2, 3.0, True, None, []
]

# Линейная структура данных
# Все элементы списка проиндексированы

a = data[1:3]

print(a)

print(list('asdfghjkl'))

# [] - False

print(bool([]))

print(data)

# append - добавить элемент в список
data.append(4)

print(data)

data.insert(0, 123)

print(data)

data.insert(4, 5)

print(data)

result = data.pop(0)
print(result)

# не рекомендуется
del data[-1]

print(data)
# Удалить элемент 2 с помощью метода pop
# Удалить None с помощью метода remove

data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
data.remove(5)

print(data)
# data.remove(6)

# in - в
print('a' in 'abcd')
my_list = ['a', 'b', 'c', 'd']
print('a' in my_list)
