first = int(input())
second = int(input())

if first % 2 != 0:
	first = first + 1

l = []
while first <= second:
	l.append(first)
	first = first + 2
print(sum(l))
