# Nhập hai số tự nhiên m và n từ bàn phím
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (n lớn hơn m): "))

# Kiểm tra xem m và n có phù hợp
if m >= n:
    print("Vui lòng nhập n lớn hơn m.")
else:
    # In ra các số chia hết cho m trong khoảng từ 1 đến n
    for i in range(1, n + 1):
        if i % m == 0:
            print(i)