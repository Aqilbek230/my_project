#1
# for i in range(1,21):  #20ga shekemgi sanlar shgadi
#     print(i)

#2
# for i in range(2,51,2):  #0den 50ge shekemgi jup sanlardi shgariw
#     print(i)

#3
# for i in range(1,51,2):  # den 50ge shekemgi taq sanlar
#     print(i)

#4
# a= int(input("a: "))
# for i in range(a,0,-1): #kiritilgen san arqaga qaraap shgadi 1ge shekem
#     print(i)


#5
# fruits = ["olma", "banan", "anor", "gilos"]
# for i in fruits:
#     print(i)


#6
# for i in range(3,100,3):  #1den 100ge shekem 3ke bolinetin sanlar
#     print(i)


#1
# a=int(input("a: "))
# if a>0:
#     print(True)
# else:
#     print(False)


#2
# a=int(input("a: "))
# if a%2==1:
#     print("a sani taq")
# else:
#     print("a sani jup")

#3
# a=int(input("a: "))
# if a%2==0:
#     print("a sani jup")
# else:
#     print("a sani taq")


#4
# a=int(input("a: "))
# b=int(input("b: "))
# if a>2 and b<=3:
#     print(True)
# else:
#     print(False)

#5
# a=int(input("a: "))
# b=int(input("b: "))
# if a>=0 or b<-2:
#     print(True)
# else:
#     print(False)


#6
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if a<=b<=c:
#     print(True)
# else:
#     print(False)

#7
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if a>b<c or c<b<a:
#     print(True)
# else:
#     print(False)
    
#8
# a=int(input("a: "))
# b=int(input("b: "))
# if a%2==1 and b%2==1:
#     print("Taq san")
# else:
#     print("Jup san)

#9
# a=int(input("a: "))
# b=int(input("b: "))
# if a%2==1 or b%2==1:
#     print("Keminde birewi taq")
# else:
#     print("Keminde birewi jup")

#10
# a=int(input("a: "))
# b=int(input("b: "))
# if (a%2==1 and b%2==0) or (a%2==0 and b%2==1):
#     print("Tek birewi taq")
# else:
#     print(False)

#11
# a=int(input("a: "))
# b=int(input("b: "))
# if (a%2==1 and b%2==1) or (a%2==0 and b%2==0):
#     print(True)
# else:
#     print(False)

#12
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if a>0 and b>0 and c>0:
#     print("hammesi on")
# else:
#     print(False)

#13
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if a>0 or b>0 or c>0:
#     print("Kemi Birewi jup")
# else:
#     print(False)

#14
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if (a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0):
#     print(True)
# else:
#     print(False)


#15
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if (a>0 and b>0 and c<0) or (a<0 and b>0 and c>0) or (a>0 and b<0 and c>0):
#     print(1)
# else:
#     print(0)

#16
# a=int(input("a: "))
# if a%2==0 and a>0 and 10 <= a <= 99:
#     print("ras")
# else:
#     print("jalgan")

#17
# a=int(input("a: "))
# if a%2==1 and a>0 and 100<=a<=999:
#     print(1)
# else:
#     print(0)

#18
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if (a==b or a==c or b==c):
#     print(1)
# else:
#     print(0)

#19
# a=int(input("a: "))
# b=int(input("b: "))
# c=int(input("c: "))
# if (a==-b or a==-c or b==-c):
#     print(1)
# else:
#     print(0)

#20
# n=int(input("a: ")) #3xanali san
# a=n//100
# b=(n//10)%10
# c=n%10
# if a!=b and a!=c and b!=c:
#     print(1)
# else:
#     print()

#21
# n=int(input("a: ")) #3xanali san
# a=n//100
# b=(n//10)%10
# c=n%10
# if a<b and b<c:
#     print(1)
# else:
#     print(0)

#22
# n=int(input("a: ")) #3xanali san
# a=n//100
# b=(n//10)%10
# c=n%10
# if (a < b and b < c) or (a > b and b > c):
#     print(1)
# else:
#     print(0)

#23
# n=int(input("m: "))
# a=n//100
# b=(n//10)%10
# c=n%10
# if a==c:
#     print(1)
# else:
#     print(0)




#XAZINANI TABIW OYINI

# print("Xazinani tabiw oyinina xosh kelibsiz!")
# print("Sizdin waziypaniz xazinani tabiw")
# tanlaw1=input("Aldinizda eki jol bar: \n'On' yaki 'shep'. Siz qaysi tarepden juresiz?\n>>> ")
# if tanlaw1=="shep":
#     print("Siz daryaga keldiniz. Suziw yaki kutiw")
#     tanlaw2=input("Siz qayiqdi kutesizba yaki darya boylap suzesizba? \nsuziw ushin 'suz', kutiw ushin 'kut' deb jazin. \n>>>")
#     if tanlaw2=="kut":
#         print("Siz xazinaga keldiniz!")
#         tanlaw3=input("Sizde 3esik bar birewin tanlan: \n>>>'kok' , 'qizil' , 'sari' \n> ")
#         if tanlaw3=="qizil":
#             print("Qizil esikde bomba bar edi. Oyin juwmaqlandi ")
#         elif tanlaw3=="sari":
#             print("Siz xazinani tapdiniz!!!")
#         elif tanlaw3=="kok":
#             print("Kok esik bos edi. Oyin juwmaqlandi ")            
#     elif tanlaw2=="suz":
#         print("Siz daryaga shogib kettiniz. Oyin juwmaqlandi!")
        
# else:
#     print("Siz oyinnan shiqtiniz")



#Uch xonali sonning raqamlari yig‘indisi
#Foydalanuvchi uch xonali son kiritsin. Uning raqamlari yig‘indisini toping.

# n=123
# a=n//100
# b=n//10%10
# c=n%10
# print(a+b+c)

# 1 dan N gacha bo‘lgan juft sonlarni chiqarish
# Foydalanuvchi N sonini kiritsin. 1 dan N gacha bo‘lgan faqat juft sonlarni ekranga chiqaring.

# n=int(input("n: "))
# for i in range(1,n+1):
#     if i%2==0:
#        print(i)

# 1 dan N gacha bo‘lgan sonlar yig‘indisini hisoblang
# For yordamida.

# n=int(input("n: "))
# a=0
# for i in range(1,n+1):
#     a+=i
# print(a)

# Foydalanuvchi kiritgan 3 ta sondan eng kattasini toping.

# a=int(input("a>>> "))
# b=int(input("b>>> "))
# c=int(input("c>>> "))
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)

# 1 dan N gacha bo‘lgan sonlar orasida nechta 
# juft va nechta toq son borligini sanang.

# N = int(input("N: "))
# jup = 0
# taq = 0
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         jup += 1
#     else:
#         taq += 1
# print("Juft sonlar:", jup)
# print("Toq sonlar:", taq)


# Foydalanuvchi kiritgan sonning barcha bo‘luvchilarini chiqarish.
# a=int(input("a>>> "))
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)


# Foydalanuvchi kiritgan son tub yoki tub emasligini aniqlang (soddaroq usul bilan).
# a=int(input("a: "))
# boliwshiler_sani=0
# for i in range(1,a+1):
#     if a%i==0:
#         boliwshiler_sani+=1
# if boliwshiler_sani==2:
#     print("Tub san")
# else:
#     print("Tub emes")



# Masala: “Maktabdagi baholarni tahlil qilish”
# Shartlar:

# Foydalanuvchi 10 ta baho kiritadi (1–5 oralig‘ida).

# Dastur quyidagilarni hisoblaydi:

# Necha ta a’lo baho (5) bor

# Necha ta yaxshi baho (4) bor

# Necha ta qoniqarli baho (3) bor

# Necha ta yomon baho (1 yoki 2) bor

# O‘rtacha bahoni hisoblaydi


# a_lo = 0
# yaxshi = 0
# qoniqarli = 0
# yomon = 0
# jami = 0

# for i in range(10):
#     baho = int(input(f"{i+1}-bahoni kiriting: "))
#     jami += baho
    
#     if baho == 5:
#         a_lo += 1
#     elif baho == 4:
#         yaxshi += 1
#     elif baho == 3:
#         qoniqarli += 1
#     else:
#         yomon += 1

# print("Alo baholar:", a_lo)
# print("Yaxshi baholar:", yaxshi)
# print("Qoniqarli baholar:", qoniqarli)
# print("Yomon baholar:", yomon)
# print("Ortacha baho:", jami/10)





# "Oylik daromad tahlili"
# Shartlar:

# Foydalanuvchi bir oy davomida 30 kunlik daromadni kiritsin.

# Dastur quyidagilarni aniqlashi kerak:

# Necha kun daromad 1000 dan kop bolgan

# Necha kun daromad 500 dan kam bolgan

# Eng yuqori daromad qaysi kunda bolgan

# Oylik jami daromad

# Ortacha kunlik daromad


# Boshlang'ich qiymatlar
# kunlar_1000_ortiq = 0
# kunlar_500_kam = 0
# eng_yuqori_daromad = 0
# eng_yuqori_kun = 0
# jami_daromad = 0

# # 30 kunlik daromadni qabul qilish
# for kun in range(1, 31):
#     daromad = int(input(f"{kun}-kun daromadni kiriting: "))
    
#     jami_daromad += daromad  # jami daromadga qo'shish

#     # 1000 dan ortiq daromad kunlari
#     if daromad > 1000:
#         kunlar_1000_ortiq += 1

#     # 500 dan kam daromad kunlari
#     if daromad < 500:
#         kunlar_500_kam += 1

#     # Eng yuqori daromad va kunni aniqlash
#     if daromad > eng_yuqori_daromad:
#         eng_yuqori_daromad = daromad
#         eng_yuqori_kun = kun

# # Oxirgi natijalarni chiqarish
# print("\n--- Oylik daromad tahlili ---")
# print("1000 dan ortiq daromad kunlari:", kunlar_1000_ortiq)
# print("500 dan kam daromad kunlari:", kunlar_500_kam)
# print("Eng yuqori daromad:", eng_yuqori_daromad, "so'm,", "kun:", eng_yuqori_kun)
# print("Oylik jami daromad:", jami_daromad, "so'm")
# print("Ortacha kunlik daromad:", jami_daromad / 30, "so'm")



# Dokondagi mahsulotlar
# Shartlar:

# Foydalanuvchi dokonga 10 ta mahsulot narxini kiritsin.

# Dastur quyidagilarni hisoblasin:

# 5000 somdan qimmatroq mahsulotlar soni

# 2000 somdan arzon mahsulotlar soni

# Eng qimmat mahsulot narxi va uning tartib raqami

# Jami narx

# Ortacha narx

# qimbat_5000_somnan=0
# arzan_2000_somnan=0
# en_qimbat_product=0
# qimbat_product_orni=0
# jami_som=0
# for baha in range(10):
#     bahasi=int(input(f"{baha+1} product bahasin kiritin: "))
#     jami_som+=bahasi
    
#     #5000nan qimbat
#     if bahasi>5000:
#         qimbat_5000_somnan+=1
    
#     #2000nan arzan
#     if bahasi<2000:
#         arzan_2000_somnan+=1
    
#     #en qimbat product
#     if bahasi>en_qimbat_product:
#         en_qimbat_product=bahasi
#         qimbat_product_orni=baha+1

# print("\n>>> Bahalar ham bahalar sani <<<")    
# print("\n5000nan qimbat productlar sani>>> ",qimbat_5000_somnan)
# print("2000nan arzan productlar sani>>> ",arzan_2000_somnan)
# print("En qimbat product bahasi>>> ",en_qimbat_product,
#       qimbat_product_orni,"nomerde jaylasqan!!!")
# print("Jami bahasi>>> ",jami_som)
# print("Ortasha bahasi",jami_som/10)



# a=int(input("A: "))
# s=1
# for i in range(1,a+1):
#     s*=i
# print(s)








