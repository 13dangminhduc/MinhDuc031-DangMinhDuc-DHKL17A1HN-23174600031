import math
a = float(input("moi nhap he so a"))
b = float(input("moi nhap he so b"))
c = float(input("moi nhap he so c"))
p=a+b+c/2
dt= math.sqrt(p*(p-a)*(p-b)*(p-c))
print("chu_vi", p)
print("dien_tich", dt)