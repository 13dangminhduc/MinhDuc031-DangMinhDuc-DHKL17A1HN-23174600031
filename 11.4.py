 #BT 4
# list number 1
list=[]
while True:
    gia_tri=int(input(" nhap gia trị:"))
    list.append(gia_tri)
    nhap_tiep=int(input("tiep tu nhap gia tri?1:co,0:khong "))
    if nhap_tiep==0:
     break
# list
x=int(input("moi nhap gia tri x:"))
print("list",list)
#tong
tong_list=sum(list)
print('tong cac gia tri xuat hien trong list la:',tong_list)
#ket qua tim x trong list
so_lan_xh=list.count(x)
print(x,'xuat hien',so_lan_xh,'lan trong list')
print(x,'khong lon hon tat ca cac so trong list')
# ca so lon hon x trong list
so_lon_hon_x = [so for so in list if so > x]
print("Các số lớn hơn", x, "trong list", so_lon_hon_x)
