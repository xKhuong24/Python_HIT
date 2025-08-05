n = int(input("Nhập số lượng phần tử trong tuple: "))
chuoi = tuple(input("Nhập các xâu ký tự số: ").split())
if len(chuoi) != n:
    print("Số lượng phần tử không khớp với n.")
else:
    tuple_moi = tuple(map(int,chuoi))
    trung_binh = sum(tuple_moi) / n
    print("Tuple ban đầu:", chuoi)
    print("Tuple sau khi chuyển:", tuple_moi)
    print("Trung bình cộng:", trung_binh)