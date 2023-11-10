# xét kết quả sử dụng hàm if....elif....else
diem_TB =  eval(input("nhập điểm trung bình: "))
if diem_TB >=0 and diem_TB <=10:
     if diem_TB < 5:
        print("yếu/kém!!!")
     elif diem_TB <6:
        print("trung_binh !!")
     elif diem_TB <7:
         print("trung bình-khá!")
     elif diem_TB <8:
        print("khá!!")
     elif diem_TB <9:
        print("gioi!!!")
     else:
        print("xuất sắc !!!!")
else:
    print("diem nhap khong hop le !")



