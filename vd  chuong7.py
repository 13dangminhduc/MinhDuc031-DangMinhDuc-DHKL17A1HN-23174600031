# vd 8.4
i=1
while i<=10 :
   print("i=", i)
   i+=1


 #vd 8.5
print("chuong trinh in ban cuu chuong")
i=1
while i<=10:
     print("3 x",i," = ", 3*i)
     i+=1
   


 #vd 8.6
for char in "uneti":
   print("character: " + char)   


#vd 8.7
sum=0
numbers = [1,2,3,4,5]
for number in numbers:
    sum+=number
print("sum = ", sum)    

#vd 8.8
numbers=[1,2,3,4,5]
animals=["dog","cat","elephant","bird","lion"]
for index in range(len(numbers)):
   print("animal["+str(index)+ "] is "+animals[index])


   # vd 8.14
   for item in range(1,10):
       if item%2==0:
           print("item", item)
   else:
       print("finish loop !")     



   # vd 8.15
   count = 1
   while count <=5:
       print(count, "<=5")
       count +=1
   else:
       print(count, "> 5")           

    # vd 8.16
   for ch in "hello python":   
        if ch =='y':
            break
        print("ký tự hiện thời: ",ch)

    #vd 8.17
   var = 10
   while var > 0:
       if var %2 == 0:
           print("giá trị : ", var) 
       var -=1
       if var ==5:
           break
   print("kết thúc vòng lặp !") 


   #vd 8.18
   for ch in "hello python":
       if ch =='y':
           continue
       print("ký tự hiện thời:",ch)    




# vd 8.19
var = 10
while var > 0:
    if var == 6:
        continue
    if var %2 == 0:
       print("giá trị : ",var)
    var -=1     


# vd 8.20
for ch in "hello python":
    if ch == 'y':
        pass#pass chỉ giữ chỗ cho for
        print("pass block")
    print("ký tự hiện thời: ", ch)
print("kết thúc vong lặp for !")
    