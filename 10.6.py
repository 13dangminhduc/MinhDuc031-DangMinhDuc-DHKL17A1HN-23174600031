# giai phuong trinh bac 2
a=int(input("moi nhap he so a:"))
b=int(input("moi nhap he so b:"))
c=int(input("moi nhap he so c:"))
#dieu kien pt bac 2
delta=b**2-4*a*c
if delta<0:
    print("phuong trinh vo nghiem")
elif delta==0:
    print("phuong trinh co nghiem kep x1,x2=",-b/2*a)
else:
    import math
    x1=(-b-math.sqrt(delta))/(2*a)
    x2=(-b+math.sqrt(delta))/(2*a)
    print("phuong trinh co hai nghiem pjhan biet")
    print("x1",x1,"x2",x2)
