N = int(input("Nhập số phần tử của list: "))
lst = []
for i in range(N):
    x = int(input(f"Nhập phần tử thứ {i + 1}: "))
    lst.append(x)
X = int(input("Nhập số X cần kiểm tra: "))
count_x = lst.count(X)
print(f"Số {X} xuất hiện {count_x} lần trong list.")
if len(lst) >= 8:
    lst[2:8] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ dài để thay thế từ vị trí 2 đến 7.")
print("List sau khi thay thế:", lst)
max_val = max(lst)
min_val = min(lst)
print(f"Số lớn nhất: {max_val}")
print(f"Số nhỏ nhất: {min_val}")
Y = int(input("Nhập số Y để chèn vào đầu list: "))
lst.insert(0, Y)
print("List sau khi chèn Y vào đầu:", lst)
is_increasing = all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))
is_decreasing = all(lst[i] >= lst[i+1] for i in range(len(lst) - 1))
if is_increasing:
    print("TĂNG")
elif is_decreasing:
    print("GIẢM")
else:
    print("NO")