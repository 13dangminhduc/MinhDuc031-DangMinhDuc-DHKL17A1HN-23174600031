# nhap so tien lai
lai_suat_mot_nam = float(input("nhap so tien lai:"))
so_tien_gui = float(input("nhap so tien gui"))
so_thang_gui = float(input("nhap so thang gui"))
tien_lai = (so_tien_gui * so_thang_gui) * (lai_suat_mot_nam/100/12)
tien_von_lai = so_tien_gui + tien_lai
print("tien_lai", tien_lai)
print("tien_von_lai", tien_von_lai)

    