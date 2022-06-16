l_1 = []
l_2 = [1, 2, 3]
l_3 = list()
l_4 = list('123')

print(l_4)

print(l_4 + l_2)
print(l_2 * 3)
print(l_2)
print(l_4)
print('3' in l_2)
print('3' in l_4)

print('12' in '123')  # True
print('12' in list('123'))  # ?

print(len(list('123456')))  # ?

l = [1, 2, 3, 4, 5]

# [4, 2]

print(l[1::2])
print(l[-2:2])
print(l[::-1])


print(l_2)
l_2.append(4)
print(l_2)
