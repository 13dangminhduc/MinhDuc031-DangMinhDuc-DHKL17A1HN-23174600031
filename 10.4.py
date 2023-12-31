#tinh bieu thuc
import math
x=int(input("moi nhap he so:"))
n=int(input("moi nhap he so:"))
A=math.pow((math.pow(x,2)+x+1),n)+math.pow((math.pow(x,2)-x+1),n)
print("A=(x**2+x+1)**n+(x**@-x+1)**n",A)