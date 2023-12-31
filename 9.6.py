# ham kiem tra so nguyen to
x=int(input("moi nhap he so:"))
if x<0:
    print("khong phai la so nguyen to")
elif x<2:
    print("khong phai la so nguyen to")
else:
    for i in range(2,x//2+1):
        if x%i==0:
            print("khong la so nguyen to")
            break
    else:
        print("la so nguyen to")