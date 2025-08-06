list1 = input(" Nhập danh sách list").split()
m = set()
for i in list1:
    for j in i:
         m.add(j)
print(list(m))
