d = [int(input("chislo = ")), int(input("chislo = ")), int(input("chislo = "))]
if d.count(d[0]) == len(d):
    print(3)
elif d.count(d[0]) == 2 or d.count(d[2]) == 2:
        print(2)
else:
    print(0)


