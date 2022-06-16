def sum_(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)
print(sum_(3, 5, 7, 8, 10, a=5, b=7, c=10))