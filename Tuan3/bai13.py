# Nhập số kWh tiêu thụ
kWh = float(input("Nhập số kWh điện tiêu thụ: "))

# Tính tiền điện
if kWh <= 50:
    tien = kWh * 1500
elif kWh <= 100:
    tien = 50 * 1500 + (kWh - 50) * 2000
else:
    tien = 50 * 1500 + 50 * 2000 + (kWh - 100) * 3000

# In kết quả
print("Tiền điện phải trả là:", tien, "đồng")