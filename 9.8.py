# kiem tra so hoan hao
n=int(input("moi nhap so hoan hao:"))
if n<0:
    print("khong la so hoan hao:")
else:
    total=0
    for i in range(1,n//2+1):
        if n%i==0:
            total+=i
    if n==total:
        print("la so hoan hao")
    else:
        print("khong la so haon hao")