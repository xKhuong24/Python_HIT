thang = int(input("Nhập tháng (1-12): "))
nam = int(input("Nhập năm: "))

# kiem tra nam nhuan
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0) :
    la_nam_nhuan = True
else:
    la_nam_nhuan = False

# so ngay trong thang
if thang == 2:
    if la_nam_nhuan:
        so_ngay = 29
    else:
        so_ngay = 28
elif thang in [4, 6, 9, 11]:
    so_ngay = 30
elif thang in [1, 3, 5, 7, 8, 10, 12]:
    so_ngay = 31
else:
    so_ngay = 0

if so_ngay == 0:
    print("Tháng không hợp lệ.")
else:
    print(f"Tháng {thang} năm {nam} có {so_ngay} ngày.")