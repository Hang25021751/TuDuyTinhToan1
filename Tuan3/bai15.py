# Nhập điểm trung bình
dtb = float(input("Nhập điểm trung bình của học sinh: "))

# Xếp loại học lực
if dtb >= 8.0:
    print("Giỏi")
elif dtb >= 6.5:
    print("Khá")
elif dtb >= 5.0:
    print("Trung bình")
else:
    print("Yếu")