a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    # Phân loại tam giác
    if a == b == c:
        print("Tam giác đều")
    elif a == b or a == c or b == c:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")