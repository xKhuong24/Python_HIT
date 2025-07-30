s1 = input("Nhập chuỗi s1: ")
s2 = input("Nhập chuỗi s2: ")
s1_reversed = s1[::-1]
print("Đảo ngược s1:", s1_reversed)
a = int(input("Nhập a (1 <= a < b): "))
b = int(input("Nhập b (a < b <= len(s2)): "))
if 1 <= a < b <= len(s2):
    s2_modified = s2[:a-1] + s2[a-1:b][::-1] + s2[b:]
    print("s2 sau khi đảo ngược đoạn từ vị trí {} đến {}:".format(a, b), s2_modified)
else:
    print("Giá trị a và b không hợp lệ!")
s3 = ''.join(s1[i] for i in range(len(s1)) if i % 2 != 0)
print("Chuỗi s3 (s1 sau khi xóa ký tự ở vị trí chẵn):", s3)
min_len = min(len(s1), len(s2))
s4 = ''.join(s1[i] + s2[i] for i in range(min_len)) + s1[min_len:] + s2[min_len:]
print("Chuỗi s4 (đan xen s1 và s2):", s4)