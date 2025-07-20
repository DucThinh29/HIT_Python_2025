for i in range(2):
    luong = int(input("Nhập lương nhân viên: "))
    if(luong >= 15000000):
        luong = luong - (luong * 30 / 100)
    elif(luong < 15000000 and luong >= 7000000):
        luong = luong - (luong * 20 / 100)
    else:
        luong = luong - (luong * 10 / 100)
    print("Luong thuc te cua nhan vien sau khi tru thue la: ", luong)