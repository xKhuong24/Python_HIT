n = int(input("Nhập số xu: "))
gia_bia = 28
so_chai = n // gia_bia
vo = so_chai
while vo >= 3:
    doi_duoc = vo // 3
    so_chai += doi_duoc
    vo = vo % 3 + doi_duoc  
print("Số chai bia có thể mua được là:", so_chai)