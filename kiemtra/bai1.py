k = tuple(input().split())
for i in range(len(k)):
    if i % 5 == 0 and i % 10 != 0:
        k.count(i)
        print(i, end = " ")
