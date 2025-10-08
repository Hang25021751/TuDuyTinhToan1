# Nhập số nguyên
n = int(input("Nhập một số nguyên: "))

# Kiểm tra bằng toán tử bitwise
if n > 0 and (n & (n - 1)) == 0:
    print(n, "là lũy thừa của 2")
else:
    print(n, "không phải là lũy thừa của 2")