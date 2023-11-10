# kiem tra co phia namn nhuan hay khong
nam = float(input("moi nhap so nam"))
# kiem tra xem do co phai nam nhuan hay khong
if (nam % 400 == 0) or ((nam % 4 == 0) and (nam & 100 != 0)):
    print("la nam nhuan")  
else:
    print("khong phai la nam nhuan")  
