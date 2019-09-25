a = int(input("storona a = "))
b = int(input("storona b = "))
c = int(input("storona c = "))

if a < b+c and b < a+c and c < a+b:
    print("YES")
else: print("NO")