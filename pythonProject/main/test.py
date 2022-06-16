import random
import time

time.time()

def generate_random_list(n):
    result = []
    for _ in range(n):
        result.append(random.randint(0, 1000))
    return result

def timer(funk):
    def wrapper(*args, **kwargs):
        one_time = time.time()
        l_1 = funk(*args, **kwargs)
        print(time.time() - one_time)
        return l_1
    return wrapper

@timer
def sorted_1(data):
    return sorted(data)

@timer
def sorted_2(data):
    data.sort()
    return data

random_list = generate_random_list(10)


print(sorted_1(random_list))
print(sorted_2(random_list))

# two_time = time.time()
# print(sorted_2(random_list))
# print(time.time() - two_time)


