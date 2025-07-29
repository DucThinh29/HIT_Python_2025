a = []
k = int(input("Nhập số lượng phần tử cho mảng a: "))
print("Nhap phan tu cho a: ")
for i in range(k):
    b = int(input())
    a.append(b)
print("Nhập só dòng và cột của ma trận: ")
n = int(input("Nhập số dòng: "))
m = int (input("Nhập số cột: "))
if(m*n>k):
    print("NO")
else:
    lst = []
    index = 0
    for i in range(n):
        dong = []
        for j in range(m):
            dong.append(a[index])
            index += 1
        lst.append(dong)
    print("Ma trận: ")
    print(lst)