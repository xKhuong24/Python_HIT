mA = int(input("Nhap so luong day a : "))
a = set()
for i in range(mA) :
    num1 = int(input(f"a[{i}] = "))
    a.add(num1)
mB = int(input("Nhap so luong day b : "))
b = set()
for i in range(mB) :
    num2 = int(input(f"b[{i}] = "))
    b.add(num2)
n = int(input("Nhap so phan tu : "))
c = []
for i in range(n) :
    num = int(input(f"c[{i}] = "))
    c.append(num)
hp = 0
for num in c :
    if num in a :
        hp += 1
    if num in b :
        hp -= 1
print(f"Muc do hanh phuc : {hp}")