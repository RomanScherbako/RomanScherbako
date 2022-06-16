def building():
    result = 5
    def var():
        nonlocal result
        result = result *6
        print(result)
    print(result)
    var()
building()