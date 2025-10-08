# Nhập hệ số a và b
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

# Giải phương trình
if a == 0:
    if b == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")
else:
    x = -b / a
    print("Nghiệm của phương trình là:", round(x, 2))