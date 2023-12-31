# viet chuong trnh xu ly chuoi sau
# tao litt
list=[74,74,72,72,73,69,69,71,76,71]
# doi inch sang met
inch=[chieu_cao*0.0254 for chieu_cao in list]
# in chieu cao trung binh,chieu cao lon nhat,chieu cao nho nhat
print("3 chieu cao dau tien:",inch[:3])
print("3 chieu cao cuoi cung:",inch[:-3])
chieu_cao_tb=sum(inch)/len(inch)
chieu_cao_lon_nhat=max(inch)
chieu_cao_nho_nhat=min(inch)

inch.sort()
print("List theo giá trị tăng dần:", inch)
inch.sort(reverse=True)
print("List theo giá trị giảm dần:", inch)