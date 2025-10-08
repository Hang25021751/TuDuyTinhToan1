# Nhập thông tin
ten = input("Tên chủ hộ: ")
chi_so_truoc = int(input("Chỉ số tháng trước: "))
chi_so_nay = int(input("Chỉ số tháng này: "))

# Tính số điện tiêu thụ
so_dien = chi_so_nay - chi_so_truoc

# Kiểm tra hợp lệ
if so_dien < 0:
    print("Chỉ số nhập không hợp lệ!")
else:
    # Tính tiền điện theo bậc
    if so_dien <= 50:
        tien = so_dien * 1984
    elif so_dien <= 100:
        tien = 50 * 1984 + (so_dien - 50) * 2050
    elif so_dien <= 200:
        tien = 50 * 1984 + 50 * 2050 + (so_dien - 100) * 2380
    elif so_dien <= 300:
        tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + (so_dien - 200) * 2998
    elif so_dien <= 400:
        tien = 50 * 1984 + 50 * 2050 + 100 * 2380 + 100 * 2998 + (so_dien - 300) * 3350
    else:
        tien = (50 * 1984 + 50 * 2050 + 100 * 2380 +
                100 * 2998 + 100 * 3350 + (so_dien - 400) * 3460)

    # Tính thêm VAT 8%
    tien_phai_tra = round(tien * 1.08)

    # In kết quả
    print("Họ và tên:", ten)
    print("Tiền phải trả là:", tien_phai_tra)
