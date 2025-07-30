a = list(map(int, input("Nhập list a, cách nhau bằng khoảng trắng: ").split()))
k = len(a)
n = int(input("Nhập số dòng n: "))
m = int(input("Nhập số cột m: "))
if n * m > k:
    print("NO")
else:
    X = []
    index = 0
    for i in range(n):
        row = []
        for j in range(m):
            row.append(a[index])
            index += 1
        X.append(row)
    print("Ma trận X({}x{}):".format(n, m))
    for row in X:
        print(row)