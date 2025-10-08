# Nhập vào một kí tự
c = input("Nhập vào một kí tự: ")
if c.isupper():  # nếu là chữ hoa
    print("Chữ thường tương ứng là:", c.lower())
elif c.islower():  # nếu là chữ thường
    print("Chữ hoa tương ứng là:", c.upper())
else:
    print("Kí tự nhập vào không phải là chữ cái.")
