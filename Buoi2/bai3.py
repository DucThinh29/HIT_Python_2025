n = int(input("Nhap n: "))
total = 0
dem = 0
while(n >= 1):
    total += int(n%10)
    dem += 1
    n = n/10
print("so chu so: ",dem)
print("Tong chu so: ",total)