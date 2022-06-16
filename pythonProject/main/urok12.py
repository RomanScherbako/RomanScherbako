import time
one = time.time()
def bar():
    print("Вывод")
    time.sleep(3)
    print("Прошло 3 секунды")
bar()
two = time.time()
print(two - one)