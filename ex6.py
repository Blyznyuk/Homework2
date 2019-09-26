b = [int(input("chislo = ")), int(input("chislo = ")), int(input("chislo = "))]
b.sort()
print(b)

print("second")
d = [int(input("chislo = ")), int(input("chislo = ")), int(input("chislo = "))]
if d[0] > d[1]:
    d[0], d[1] = d[1], d[0]
if d[1] > d[2]:
    d[1], d[2] = d[2], d[1]
if d[0] > d[1]:
    d[0], d[1] = d[1], d[0]

print(d)
