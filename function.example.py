"""
            Seylbekov Aqilbek
                            funkciyaga tiykarlangan misallar
                                                                12.12.2025

                                                                           """

"""Return boyinsha maseleler"""
#sannin kvadratin qaytaratin funkciya
def kvadrati(a):
    return a**2
# print(kvadrati(5))

#ush san beriledi en ulkeni shigiwi kerek
def en_ulkeni(a,b,c):
    maxx=a
    if b>maxx:
        maxx=b
    if c>maxx:
        maxx=c
    return maxx
# print(en_ulkeni(5,6,7))

#jup yaki taq
def jup_taq(a):
    if a%2==0:
        return "Jup"
    else:
        return "Taq"
# print(jup_taq(5))

#neshe harip bar ekenligin shigaradi
def haripler(soz):
    s=0
    for i in soz:
        s+=1
    return s
# print(haripler("Aqilbek"))

#on san teris san yaki 0ge ten ekenin aniqlaydi
def on_teris(a):
    if a>0:
        return "On san"
    if a<0:
        return "Teris san"
    if a==0:
        return "0ge ten"
# print(on_teris(0))

#kiritilgen eki sannan ulkenin qaytaradi
def ulkeni(a,b):
    if a>b:
        return a
    if b>a:
        return b
# print(ulkeni(8,9))

#Matn uzunligi 5 dan katta yoki emasligini return qiling.
def ulken_5den(l):
    s=0
    for i in l:
        s+=1
    if s>=5:
        return "tekst 5den uzin"
    else:
        return "tekst 5den kishi"
# print(ulken_5den("Aqilbek"))
#2variant
# def ulken_5den(l):
#     if len(l) >= 5:
#         return "tekst 5den uzin"
#     else:
#         return "tekst 5den kishi"

#Sonning darajasini hisoblab return qiling (a**b).
def dareje(a,b):
    return a**b
# print(dareje(5,2))

#Sonning ildizini qaytaradigan funksiya yozing.
def ildiz(a):
    return a**0.5
# print(ildiz(49))

#Son faktorialini return qiling.
# def faktorial(n):
#     if n == 0 or n == 1:    # 0! = 1, 1! = 1
#         return 1
#     else:
#         return n * faktorial(n-1)   # Rekursiya: o‘zini chaqiradi
# print(faktorial(8))

#Ro‘yxatdagi elementlar yig‘indisini return qiling.
def qosindi(lst):
    d=0
    for i in lst:
        d+=i
    return d
# print(qosindi([1,2,3,4,5,6,7,8,9]))

#Ro‘yxatdagi eng kichik sonni qaytaring.
def kishisi(lst):
    minn=lst[0]
    for i in lst:
        if i<minn:
            minn=i
    return minn
# print(kishisi([1,2,3,4,5,6]))

#Ismga "Salom, ..." qaytaradigan funksiya yozing.
def ismi(ism):
    return f"Salem {ism}"
# print(ismi("Aqilbek"))

"""List qaytaratin masleler"""
#0 dan n gacha bo‘lgan juft sonlar ro‘yxatini qaytaring.
# def jup_san(lst):
#     juppp=[]
#     for i in lst:
#         if i%2==0:
#             juppp.append(i)
#     return juppp
# print(jup_san([1,2,3,4,5]))

#1 dan n gacha toq sonlar ro‘yxatini qaytaring.
# def taq_san(lst):
#     taqq=[]
#     for i in range(1,lst+1):
#         if i%2==1:
#             taqq.append(i)
#     return taqq
# print(taq_san(7))

#Ro‘yxatdagi musbat sonlarni qaytaruvchi funksiya yozing.
# def on_san(s):
#     on=[]
#     for i in s:
#         if i>0:
#             on.append(i)
#     return on
# print(on_san([1,-4,-5,7,-2,-45,]))

#Ro‘yxatda faqat matn bo‘lgan elementlarni qaytaring.
# def tek_tekst(lst):
#     natije = []
#     for i in lst:
#         if type(i) == str:
#             natije.append(i)
#     return natije
#
# print(tek_tekst([1, "salem", 3.5, "python", True, "AI"]))

#1 dan 10 gacha bo‘lgan sonlarning kvadratlari ro‘yxatini qaytaring.
# def kvadrati(lst):
#     natijesi=[]
#     for i in range(1,lst+1):
#         natijesi.append(i**2)
#     return natijesi
# print(kvadrati(5))

#Berilgan ro‘yxatni teskari qilib qaytarish.
# def teskari(lst):
#     natije=[]
#     for i in lst:
#         natije.append(i)
#     return natije[::-1]
# print(teskari([1,2,3,4,5]))

#Matndagi harflarni ro‘yxat ko‘rinishida qaytarish.
# def harip(b):
#     jiyna=[]
#     for i in b:
#         jiyna.append(i)
#     return jiyna
# print(harip("Aqilbek"))

#Matndagi har bir harfni 2 marta takrorlab ro‘yxat qaytarish.
# def harib(b):
#     jiyna=[]
#     for i in b:
#         jiyna.append(i*2)
#     return jiyna
# print(harib("Aqilbek"))

#Ro‘yxatdagi faqat takrorlanmaydigan elementlarni qaytarish.
# def takrarlanbaytin(lst):
#     natije=[]
#     for i in lst:
#         sanaq=0
#         for j in lst:
#             if j==i:
#                 sanaq+=1
#         if sanaq==1:
#             natije.append(i)
#     return natije
# print(takrarlanbaytin([1,2,3,4,4,2,5,6,4,7,8]))

#Ikki ro‘yxatni birlashtirib qaytarish.
# def dizimler(lst1,lst2):
#     natije=[]
#
#     for i in lst1:
#         natije.append(i)
#     for j in lst2:
#         natije.append(j)
#     return natije
# print(dizimler([1,2,3],[4,5,6]))

#Ro‘yxatdagi juft indeksdagi elementlarni qaytaring.
# def jup_index(lst):
#     natije=[]
#     for i in range(len(lst)):
#         if i%2==0:
#             natije.append(lst[i])
#     return natije
# print(jup_index([1,2,3,4,5]))

#Ro‘yxatdagi toq indeksdagi elementlarni qaytaring.
# def taq_inex(lst):
#     natije=[]
#     for i in range(len(lst)):
#         if i%2==1:
#             natije.append(lst[i])
#     return natije
# print(taq_inex([1,2,3,4,8,6,5]))

# Matndagi so‘zlarni (split) ro‘yxat qilib qaytaring.
# def sozz(tekst):
#     return tekst.split()
# print(sozz("Menin atim Aqilbek"))

#Ro‘yxatdan faqat 5 dan katta sonlarni qaytaring.
# def dizimm(lst):
#     list1=[]
#     for i in lst:
#         if i>5:
#             list1.append(i)
#     return list1
# print(dizimm([5,6,9,3,2,76,64,2,3]))

#Ro‘yxatdagi har bir sonning kvadrati + 1 qiymatini qaytarish.
# def kvadratlari(lst):
#     list2=[]
#     for i in lst:
#         list2.append((i**2)+1)
#     return list2
# print(kvadratlari([1,2,3,4,5,6]))

"""Dictionary qaytaratin esaplar"""
#Ikki son beriladi — ularning yig‘indi, ayirma, ko‘paytma, bo‘linmasini dict qilib qaytaring.
# def eki_san(a,b):
#     san={
#         'kobeymesi':a*b,
#         'boliniwi':a/b,
#         'qosindisi':a+b,
#         'ayirmasi':a-b
#     }
#     print(san)
# eki_san(6,2)

#Ism va yosh kiritiladigan funksiya — {"ism":..., "yosh":...} qaytarsin.
# def ism_jas(ism,jas):
#     ati_jasi={
#         "ati":ism,
#         "jasi":jas
#     }
#     return ati_jasi
# print(ism_jas("Aqil",19))

#Matndagi harflar sonini dict qilib qaytaring (harf : soni)
# def harip_sani(ism):
#     sani={
#         'harib':ism
#     }
#     return len(ism)
# print(harip_sani("Aqilbek"))

#Ro‘yxatdagi eng katta va eng kichik sonni dict qilib qaytarish.
# def diziml(lst):
#     if not lst:
#         return {}
#     min_san=lst[0]
#     max_san=lst[0]
#     for i in lst:
#         if i<min_san:
#             min_san=i
#         if i>max_san:
#             max_san=i
#     return f"min san {min_san}, max san {max_san}"
# print(diziml([1,2,3,4,5,6]))

# def diziml(lst):
#     return f"min {min(lst)}, max {max(lst)}"
# print(diziml([3,5,8,4,2]))

#Talaba haqida dict qaytarish: ism, kurs, baho.
# def talaba(ism,kurs,baha):
#     return {"ati":ism,"kursi":kurs,"bahasi":baha}
# print(talaba("Aqilbek",3,5))

#Son juft/toq va uning kvadratini bir dictda qaytarish.
# def jup_taq(a):
#     if a%2==0:
#         return {"tip":'jup san',"kvadrati":a**2}
#     elif a%2==1:
#         return {"tip":'taq san',"kvadrati":a**2}
# print(jup_taq(5))
# print(jup_taq(6))

#Ro‘yxatdagi elementlar soni, yig‘indisi, o‘rtachasini dict qaytarish.
# def dizimler(lst):
#     return {"elementler sani":len(lst),"jami qosindisi":sum(lst),"Ortashasi":sum(lst)/len(lst)}
# print(dizimler([1,2,3,4]))

#Ism va familiyadan {"toliq_ism": "..."} dict qaytarish.
# def ism_fam(toliq_ism,fam):
#     return {"Toliq ati":f"{toliq_ism} {fam}"}
# print(ism_fam("Aqilbek","Seylbekov"))

#3 ta sonning tartiblangan natijasini dict qilib qaytarish.
# def tartiplengen(a,b,c):
#     lst=[a,b,c]
#     lst.sort(reverse=True) #ulkennen kishige qarab shgadi
#     return {"ulkeni":lst[0],"ortashasi":lst[1],"kishisi":lst[2]}
# print(tartiplengen(5,6,7))

#So‘zlar ro‘yxatidan har bir so‘z uzunligini dict qaytarish.


# def paydalaniwshi(ati,familiyasi,t_jili,t_jeri,email,tel=None):
#     paydalan={
#         'ati':ati,
#         'familiyasi':familiyasi,
#         't_jili':t_jili,
#         't_jeri':t_jeri,
#         'email':email,
#         'tel':tel
#     }
#     return paydalan
# paydalaniwshi1=paydalaniwshi("Aqilbek","Seylbekov",2006,"Nukus","aqilbek@gamil")
# paydalaniwshi2=paydalaniwshi("Jasurbek","Qadirbergenov",2005,"Shomanay","jasur@",912345)
# paydalaniwshilar=[paydalaniwshi1,paydalaniwshi2]
# for paydalan in paydalaniwshilar:
#     if paydalan['tel']:
#         tel=paydalan['tel']
#     else:
#         tel="Belgisiz"
#     print(f"{paydalan['ati']} "
#           f"{paydalan['familiyasi']} "
#           f"{paydalan['t_jili']} "
#           f"{paydalan['t_jeri']}"
#           f"{paydalan['email']} "
#           f"{tel}")

# def araliq(min,max):
#     sanlar=[]
#     while min<max:
#         sanlar.append(min)
#         min+=1
#     return sanlar
# print(araliq(0,10))
