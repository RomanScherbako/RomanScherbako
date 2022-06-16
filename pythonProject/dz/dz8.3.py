counter = {
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16,
}
counter2 = {}
for item in counter:
    counter2[counter[item]] = item
print(counter2)
