a = int(input("nhap vao chieu rong:"))
b = int(input("nhap vao chieu dai:")) 
# diện tích hình chữ nhật 
s1 = a*b 
# diện tích hình tròn 
s2 = 3.14 * (a/2)**2
Dien_tich_trong_cay= s1-s2 
print(round(Dien_tich_trong_cay , 2))