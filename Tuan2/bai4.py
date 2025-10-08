# Nhập vào một kí tự
c = input("Nhập vào một kí tự: ")

# Kiểm tra xem có phải là chữ cái không
if c.isalpha():  # nếu là ký tự chữ cái (hoa hoặc thường)
    print(f"{c} là kí tự alphabet")
else:
    print(f"{c} không phải là kí tự alphabet")
