ban1 = set(input("Nhập mã sinh viên tại bàn 1: ").split())
ban2 = set(input("Nhập mã sinh viên tại bàn 2: ").split())
print("Danh sách bàn 1:", ban1)
print("Danh sách bàn 2:", ban2)
giao = ban1.intersection(ban2)
if giao:
    print("Sinh viên đăng ký tại cả hai bàn:", giao)
else:
    print("Không có sinh viên nào đăng ký tại cả hai bàn.")
tong_hop = ban1.union(ban2)
print("Danh sách tổng hợp các sinh viên đăng ký:", tong_hop)
khac = ban1.difference(ban2)
print("Sinh viên chỉ đăng ký tại bàn 1:", khac)