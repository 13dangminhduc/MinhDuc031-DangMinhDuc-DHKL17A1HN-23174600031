n = float(input("moi nhap he so n:"))
kt=True
if n < 2: kt=False
for i in range(2,n//2+1):
   if n%i==0 : kt=False
if kt==True:
   print("la so nguyen to")
else: 
   print("khong la so nguyen to")