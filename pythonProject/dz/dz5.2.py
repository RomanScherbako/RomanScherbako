l_1 = []
for ithem in range(1, 100):
    if ithem == 3 or ithem == 2 or ithem == 5 or ithem == 7:
        l_1.append(ithem)
    if ithem % 5 != 0 and ithem % 3 != 0  and ithem % 2 != 0 and ithem % 7 != 0 and ithem != 1:
        l_1.append(ithem)
print(l_1)