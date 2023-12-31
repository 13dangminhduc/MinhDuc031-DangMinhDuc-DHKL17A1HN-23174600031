# nhap chuoi
s=int(input("moi nhap chuoi s:"))
s_sub=int(input("moi nhap chuoi s_sub"))
s_find=int(input("moi nhapc huoi s_find"))
s_replace=int(input("moi nhap chuoi s_replace"))
print("xuat ra s",s)

#loai bo khoang trang o dau va cuoi chuoi
s=s.strip()
print("sau khi loai bo ta duoc:",s)

#in chuoi ky tu dau va cuoi viet joa
s=s.capitalize()
print("ky tu viet hoa la:",s)

#dem va in ra s_sub xuat hien s
s=s.count()
print("s_sub xuat hien la:",s)

# tim kiem va thay the
s=s.s_replace(s_find,s_replace)
print("tim kiem va thay the",s)
