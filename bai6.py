import math  # dùng để tính căn bậc hai

# Nhập vào 3 cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện là 3 cạnh của tam giác
if a + b > c and a + c > b and b + c > a:
    # Tính nửa chu vi
    p = (a + b + c) / 2

    # Áp dụng công thức Heron để tính diện tích
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))

    # In ra kết quả với 1 chữ số thập phân
    print("Diện tích tam giác là: {:.1f}".format(S))
else:
    print("Khong phai 3 canh cua tam giac")