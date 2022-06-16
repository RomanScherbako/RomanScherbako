#counter = 1
#while counter <= 5:
#    print(counter)
 #   counter += 1

sum_ = 0
while True:
    a = int(input())
    if a < 0:
        sum_ = (a * 2) + sum_
        continue
    elif a == 0:
        break
print(sum_)