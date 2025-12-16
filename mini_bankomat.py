#Mini bankomat dasturi

# balanis=100000
# pin=2025
# parol=0
# max_parol=3
# istoriya=[]
# while parol<3:
#     pin_k=int(input("Pin kodinizdi kiritin(3marte qate terilse bloklanadi): "))
#     if pin_k==pin:
#         while True:
#             print("\n1.Balansdi koriw ushin 1.")
#             print("2.Naqd pul sheshiw ushin 2.")
#             print("3.Paroldi koriw ushin 3.")
#             print("4.Balanisdi toltiriw ushin 4.")
#             print("5.Istoriyani koriw ushin 5.")
#             print("6.Pin kodti ozgetiw 6.")
#             print("0.Shigiw ushin 0.")
#             kiritin=int(input("\nKiritin(san boliwi kerek(0-6): "))
#
#             if kiritin==0:
#                 print("Plastik qaytarildi")
#                 exit()
#
#             elif kiritin==1:
#                 print(f"Sizdin balanisizda {balanis} sum bar")
#
#             elif kiritin==2:
#                 print(f"Balanisizda {balanis} sum bar.")
#                 sumdi=int(input("Qansha sheshemiz: "))
#                 if sumdi<=balanis:
#                     sora=input("Naq puldi aniq sheshemizba (awa/yaq):").lower()
#                     if sora=='awa':
#                         balanis-=sumdi
#                         istoriya.append(f"Balanisdan {sumdi} sum sheshildi")
#                         print(f"Balanisdan {sumdi} sum sheshildi")
#                         print("balanisda jami",balanis,"sum bar")
#
#                     else:
#                         print("Naq pul sheshiw toqtatildi")
#                 else:
#                     print("Balanisizda pul jeterli emes!")
#
#             elif kiritin==3:
#                 print("Sizdin paroliniz",pin)
#
#             elif kiritin==4:
#                 toltir=int(input("Balanisqa qansha salamiz: "))
#                 balanis+=toltir
#                 istoriya.append(f"Balanisqa {toltir} sum qosildi")
#                 print(f"Balanis {toltir} summaga toldi")
#                 print("Balanisinizda jami",balanis,"sum bar")
#
#             elif kiritin==5:
#                 if not istoriya:
#                     print("Ele ameliyat joq")
#                 else:
#                     for s in istoriya:
#                         print(s)
#             elif kiritin == 6:
#                 eski_pin = int(input("Eski PIN kodti kiritin: "))
#
#                 if eski_pin == pin:
#                     taza_pin = int(input("Taza PIN kodti kiritin: "))
#                     aniqba = int(input("Taza PIN kodti qayta kiritin: "))
#
#                     if taza_pin == aniqba:
#                         pin = taza_pin
#                         print("PIN ozgertildi")
#                     else:
#                         print(" Eki pin kod bir birine tuwri kelmeydi")
#                 else:
#                     print("Eski PIN qate!")
#
#             else:
#                 print("Qate kiritiw. Qaytaldan kiritin(0-3)")
#     else:
#         # print("Pin kod qate! 3marte qate terilse karta bloklanadi")
#         parol+=1
#         qalgani=max_parol-parol
#         if qalgani>0:
#             print('pin kod qate.',qalgani,'urinis qaldi')
#         else:
#             print("Karta bloklandi")
#             exit()