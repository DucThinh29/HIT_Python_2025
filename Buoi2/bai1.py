for i in range(4):
    thang = int(input("Nhập tháng: "))
    nam = int(input("Nhập năm: "))

    if(thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12 and nam%4 != 0):
        print("31 ngày")
    elif(thang == 4 or thang == 9 or thang == 6 or thang == 11 and nam %4 != 0):
        print("30 ngày")
    elif(thang == 2 and nam %4 != 0):
        print("28 ngày")
    else:
        print("29 ngày")