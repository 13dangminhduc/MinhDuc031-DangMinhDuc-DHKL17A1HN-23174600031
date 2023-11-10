# Nhập một số từ bàn phím
so = float(input("Nhập một số: "))

# Kiểm tra xem số đó có phải là số dương hay không
if so > 0:
    # Tính bình phương của số và in ra
    binh_phuong = so**2
    print(f"Bình phương của {so} là {binh_phuong}")
else:
    print(f"{so} không phải là số dương.")
    