# Nhập số nguyên dương n (năm)
n = int(input("Nhập năm: "))

# Kiểm tra năm nhuận
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("Yes")
else:
    print("No")