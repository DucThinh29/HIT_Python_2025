xu = int(input("Nhập số tiền cho trước: "))
ketqua = 0
vochai = 0
while((xu-28) >= 0):
    xu -= 28
    ketqua += 1
    vochai += 1
    if(vochai == 3):
        ketqua += 1
        vochai = 0
print("Số chai mua được là: ",ketqua)
