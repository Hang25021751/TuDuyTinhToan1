# Nhập hai số
m = float(input("Nhập số m: "))
n = float(input("Nhập số n: "))
# Kiểm tra tránh chia cho 0
if n == 0:
    print("Không thể chia cho 0!")
else:
    kq = m // n
    print("Kết quả làm tròn xuống của", m, "/", n, "là:", kq)