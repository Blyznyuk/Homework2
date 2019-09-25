a = input('рандомная строка для определение является ли строка числа:' )
print(a.isdigit())


b = input('рандомная строка для подсчета пробелов и точек:' )
print('Количество пробелов:', b.count(' '))
print('Количество точек:', b.count('.'))


c = "Homework"
print("100 and homework", c.center(100))
print("100 and homework", ' '*((100-len(c))//2), c, ' '*((100-len(c))//2))


d = input('random string:' )
print("pervaya bukva", d.title())
