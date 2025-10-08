n = int(input("Nhập số nguyên n: "))

am = n < 0
n = abs(n)
dao = 0

while n != 0:
    dao = dao * 10 + n % 10
    n //= 10

if am:
    dao = -dao

print("Số đảo ngược là:", dao)
