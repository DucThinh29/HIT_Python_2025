N = int(input("Nhập số lượng phần tử: "))
lst = []
#1
print("Nhap phan tu:")
for i in range(N):
    a = int(input())
    lst.append(a)
print(lst)
#2
X = int(input("Nhập số nguyên X: "))
print("Số lần xuất hiện số X trong list là:",lst.count(X))
#3 thay phan tu tu vi tri 2-7 ->[]
thay = [8, 5, 4, 0, 1, 3]
lst[1:7] = thay
print(lst)
#4
print("So lon nhat trong list là:",max(lst))
print("So nho nhat trong list là:",min(lst))
#5
Y = int(input("Nhập số Y: "))
lst.insert(0,Y)
print(lst)
#6
lstcopy1 = lst
lstcopy2 = lst
lstcopy1.sort()
lstcopy2.sort(reverse=True)

if(lst == lstcopy1):
    print("Tăng")
elif(lst == lstcopy2):
    print("Giảm")
else:
    print("No")