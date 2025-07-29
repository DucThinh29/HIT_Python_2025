#1
s1 = str(input("Nhập chuỗi s1: "))
s2 = str(input("Nhập chuỗi s2: "))

#2
print("Đảo ngược của chuỗi s1: " + s1[::-1])

#3
print("Nhập 1 <= a < b <= độ dài s2:")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if(1 <= a and a < b and b <= len(s2)):
    news2 = s2[0:a-1] + s2[a-1:b][::-1] + s2[b:]
    print("Chuỗi s2 sau khi đảo ngược vị trí từ a đến b là: " + news2)

#4 In ra chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn.
s3 = s1[0:len(s1):2]

print("Chuỗi s3 sau khi xóa phần tử chẵn s1: " + s3)
#5 trả về chuỗi s4 đan xem kí tự giữa s1 và s2
n = min(len(s1),len(s2))
s4 = ""
for i in range(n):
    s4 += s1[i] + s2[i]
if(len(s1) < len(s2)):
    s4 += s2[len(s1):]
    print("Chuỗi s4 sau khi đan xen là: "+ s4)
elif(len(s1)>len(s2)):
    s4 += s1[len(s2):]
    print("Chuỗi s4 sau khi đan xen là: "+ s4)
else:
    print("Chuỗi s4 sau khi đan xen là: "+ s4)


