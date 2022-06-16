year = int(input('Введите год: '))
def bissextile(year):
    if year % 4 == 0 and year % 100 != 0:
        return bool(year)
    elif year % 400 == 0:
        return bool(year)
    else:
        year = 0
        return bool(year)
print(bissextile(year))