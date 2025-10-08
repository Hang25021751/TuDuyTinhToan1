import math

# Nhập hai số
m = float(input("Nhập số m: "))
n = float(input("Nhập số n: "))

# Kiểm tra chia cho 0
if n == 0:
    print("Không thể chia cho 0!")
else:
    kq = math.ceil(m / n)
    print("Kết quả làm tròn lên của", m, "/", n, "là:", kq)