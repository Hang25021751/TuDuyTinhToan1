# Nhập vào một chữ cái hoa
c = input("Nhập vào một chữ cái hoa: ")

# Kiểm tra và xử lý
if c == 'A':
    print("Không có chữ cái thường liền trước chữ cái 'a'. (Vì 'A' là chữ cái đầu tiên)")
elif c.isupper():  # nếu là chữ hoa khác 'A'
    # Chuyển sang chữ thường và tìm chữ cái liền trước
    chu_thuong_truoc = chr(ord(c.lower()) - 1)
    print("Chữ cái thường liền trước là:", chu_thuong_truoc)
else:
    print("Kí tự nhập vào không phải là chữ cái hoa.")