def chuan_hoa_ho_ten(ten):
    tu = ten.strip().lower().split()
    tu_chuan = [word.capitalize() for word in tu]
    return ' '.join(tu_chuan)
ten_input = input("Nhập họ tên: ")
ten_chuan = chuan_hoa_ho_ten(ten_input)
print("Tên đã chuẩn hóa:", ten_chuan)
