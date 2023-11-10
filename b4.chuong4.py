# nhap ba so tu ban phim
so_1 = float(input("nhap so thu nhat:"))
so_2 = float(input("nhap so thu hai:"))
so_3 = float(input("nhap so thu ba:"))
so_lon_nhat = so_1
# kiem tra m va n co phu hop
if so_2 > so_lon_nhat:
    so_lon_nhat = so_2
if so_3 > so_lon_nhat:
    so_lon_nhat = so_3
print(f"so lon nhat trong ba so la: {so_lon_nhat}")