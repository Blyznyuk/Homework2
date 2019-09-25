a = int(input("chislo a = "))
b = int(input("chislo b = "))
c = int(input("chislo c = "))

d = [a, b, c]

if d.count(a) == len(d):
    print(3)
elif d.count(a) == 2 or d.count(b) == 2:
        print(2)
else:
    print(0)
