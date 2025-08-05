n = int(input("Nhập số phần tử của mảng a: "))
a = []
for i in range(n):
    s = input(f"Nhập phần tử thứ {i }: ")
    a.append(s)

b = tuple(a)
print("Tuple b:", b)
count = 0
for item in b:
    if item.isdigit():  
        count += 1

print("Số phần tử có dạng số trong tuple b là:", count)