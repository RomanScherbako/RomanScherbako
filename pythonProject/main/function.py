# a = 3
# b = 4
# c = 5
# d = 6
# def my_max(a, b):
#     if a > b:
#         return a
#     return b
#
#
# def m_max4(a, b, c, d):
#     if my_max(a, b) > my_max(c, d):
#         return my_max(a, b)
#     return my_max(c, d)
# print(m_max4(a, b, c, d))


counter = 0
numbers = [6, 3, 8, 2, 8, 3, 5, 9, 12, 33, 2, 3, 7, 5, 9]
# for ithem in numbers:
#     if ithem > counter:
#         counter = ithem
# print(counter)
def my_max_n(numbers):
    result = numbers[0]
    for ithem in numbers:
        if ithem > result:
            result = ithem
    return result
print(my_max_n(numbers))





