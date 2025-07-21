luong = int(input("nhap luong cua nhan vien: "))
if luong >= 15000000:
    thue = luong * 0.3 
    thu_nhap = luong - thue
elif luong >= 7000000: 
    thue = luong * 0.2
    thu_nhap = luong - thue
elif luong >0:
    thue = luong * 0.1
    thu_nhap = luong - thue
else:
    print ("hay nhap lai luong!") 
print("Thue =", int(thue ) ,"va Thu nhap = ", int(thu_nhap))