import datetime
import locale
day = int(input("Nhập ngày:"))
month = int(input("Nhập tháng:"))
year = int(input("Nhập năm:"))
#Xuất theo định dạng ngày-tháng-năm
date = datetime.datetime(year,month,day)
print("Ngày tháng năm vừa nhập: ", date.strftime("%d-%m-%Y"))
# tinh ngay trong tuan
weekday=date.strftime("#A")
print(date.strftime("%d-%m-%y"),"là",weekday)
# kiem tra do phai nam nhuan hay khong
if year%4==0 and year%100!=0 or year%400==0:
    print("la nam nhuan:")
else:
    print("khong la nam nhuan:")
# hco biet thang nhap vao co bao nheiu ngay
if month==2:
    if year%4==0 and year%100!=0 or year%400==0:
        ngay_trong_thang=29
    else:
        ngay_trong_thang  = 28
elif month in [4,6,8,11]:
    ngay_trong_thang=30
else:
    ngay_trong_thang=31
    print("thang",month,"co",ngay_trong_thang,"ngay")
