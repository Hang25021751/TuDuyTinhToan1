# Nhập hai số
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

print("Trước khi hoán đổi: a =", a, ", b =", b)

# Hoán đổi bằng phép XOR
a = a ^ b
b = a ^ b
a = a ^ b

print("Sau khi hoán đổi: a =", a, ", b =", b)