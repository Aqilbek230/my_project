from operator import index
from typing import reveal_type


class Avto():
    def __init__(self,model,reni,bahasi):
        self.model=model
        self.reni=reni
        self.__bahasi=bahasi
        
    def get_info(self):
        return f"Modeli:{self.model},reni:{self.reni},bahasi:{self.__bahasi}$"
    def get_bahasi(self):
        return self.__bahasi
        
class ElektrAvto(Avto):
    def __init__(self, model, reni, bahasi,batariya):
        super().__init__(model, reni, bahasi)
        self.batariya=batariya
        
    def get_info(self):
        return f"Modeli: {self.model},reni: {self.reni},bahasi: {self.get_bahasi()}$,batariya zaryadi:{self.batariya} "
    
salon_mashinlari=[Avto("Cobalt","Aq",1000),
                  Avto("Jentra", "Qara", 1500),
                  ElektrAvto("BYD", "Kok", 2000, 1500) 
                  ]
klient_balans=3000
while True:
    print("Avto salonimizga xosh kelibsiz!")
    print(f"Sizdin balanisinizda {klient_balans}$ bar")
    print("\n1. Mashinalardi koriw")
    print("2. Mashin satip aliw")
    print("3. Shigiw")
    
    tanlaw=int(input("Tanlaw kiritin(1-3): "))
    if tanlaw==1:
        n=1
        for i in salon_mashinlari:
            print(f"{n}. {i.get_info()}")
            n=n+1
    elif tanlaw==2:
        n=1
        for i in salon_mashinlari:
            print(f"{n}.Modeli: {i.model}, bahasi: {i.get_bahasi()}$")
            n=n+1
        
        
        kiritin=int(input("Satip almaqshi bolgan mashin id kiritin: "))
        index=kiritin-1
        mashin=salon_mashinlari[index]

        if klient_balans>=mashin.get_bahasi():
            klient_balans=klient_balans-mashin.get_bahasi()

            salon_mashinlari.remove(mashin)
            print(f"Qutliqlaymiz! Siz {mashin.model} mashinin satip aldiniz")
        else:
            print("Sizdin balanisinzda pul jeterli emes")

    elif tanlaw==3:
        print("Raxmet!")
        break

    else:
        print('Qate tanlaw')




