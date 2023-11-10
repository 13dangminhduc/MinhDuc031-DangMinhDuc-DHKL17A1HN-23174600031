# Hàm tính UCLN (Ước chung lớn nhất)
def UCLN(a, b):
    while b:
        a, b = b, a % b
    return a
# Nhập hai số từ bàn phím
so1 = int(input("Nhập số thứ nhất: "))
so2 = int(input("Nhập số thứ hai: "))
# Tính BCNN sử dụng công thức
bcnn = (so1 * so2) // UCLN(so1, so2)
# In ra BCNN của hai số
print("BCNN của", so1, "và", so2, "là:", bcnn)