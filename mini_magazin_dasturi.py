import datetime

products = [
    {"code": 1, "name": "Alma", "bahasi": 5000, "danasi": 14},
    {"code": 2, "name": "Notebook", "bahasi": 5000, "danasi": 24},
    {"code": 3, "name": "Koylek", "bahasi": 120, "danasi": 15},
]

sales_history = []

while True:
    print("\n1. Productdi koriw")
    print("2. Productdi redaktorlaw")
    print("3. Productdi oshiriw")
    print("4. Product qosiw")
    print("5. Product satiw")
    print("6. Esabat")
    print("0. Shıǵıw")

    tanlov = input("Kiritin (0-6): ").strip()

    if tanlov == "0":
        print("Programmadan shıqtınız. Raxmet!")
        break

    elif tanlov == "1":
        if not products:
            print("Product joq.")
        else:
            print("\nProductlar dizimi:")
            for p in products:
                print(f"Code: {p['code']} | {p['name']} | Bahasi: {p['bahasi']} | Soni: {p['danasi']}")

    elif tanlov == "2":
        if not products:
            print("Redaktorlaw ushin product joq.")
            continue

        for p in products:
            print(f"Code: {p['code']} | {p['name']} | Bahasi: {p['bahasi']} | Soni: {p['danasi']}")

        try:
            code = int(input("Qaysi product codeni redaktorlaysiz?: "))
        except ValueError:
            print("Code san boliwi kerek!")
            continue

        product = next((p for p in products if p['code'] == code), None)
        if not product:
            print("Bunday code bar product tabilmadi.")
            continue

        print(f"Tanlangan: {product['name']} (bahasi: {product['bahasi']}, sani: {product['danasi']})")

        yangi_name = input("Jana name (bos qaldirsa ozgermeydi): ").strip()
        yangi_bahasi = input("Jana bahasi (bos qaldirsa ozgermeydi): ").strip()
        yangi_danasi = input("Jana sani (bos qaldirsa ozgermeydi): ").strip()

        try:
            if yangi_name:
                product['name'] = yangi_name
            if yangi_bahasi:
                product['bahasi'] = int(yangi_bahasi)
            if yangi_danasi:
                new_qty = int(yangi_danasi)
                old_qty = product['danasi']
                farq = new_qty - old_qty
                if farq > 0:
                    print(f"➕ {farq} ta qoshildi.")
                elif farq < 0:
                    print(f"➖ {abs(farq)} ta kamaydi.")
                product['danasi'] = new_qty
            print("Product janalandi.")
        except ValueError:
            print("Kiritilgen magliwmat duris emes.")

    elif tanlov == "3":
        if not products:
            print("Oshiriw ushin product joq.")
            continue

        for p in products:
            print(f"Code: {p['code']} | {p['name']} | Bahasi: {p['bahasi']} | Soni: {p['danasi']}")

        try:
            code = int(input("Qaysi product codeni oshiresiz?: "))
        except ValueError:
            print("Code san boliwi kerek!")
            continue

        product = next((p for p in products if p['code'] == code), None)
        if not product:
            print("Bunday code bar product tabilmadi.")
            continue

        products.remove(product)
        print(f"🗑 {product['name']} product oshirildi.")

    elif tanlov == "4":
        yangi_name = input("Product name: ").strip()
        if not yangi_name:
            print("Product name kiritilmedi!")
            continue

        mavjud = next((p for p in products if p['name'].lower() == yangi_name.lower()), None)
        if mavjud:
            try:
                yangi_danasi = int(input(f"{mavjud['name']} bar edi ({mavjud['danasi']} dana). Qansha qosamiz?: "))
                if yangi_danasi < 1:
                    print("Miqdor 0 dan ulken boliw kerek.")
                    continue
            except ValueError:
                print("Miqdor san boliwi kerek!")
                continue
            mavjud['danasi'] += yangi_danasi
            print(f"✅ {mavjud['name']} sani {yangi_danasi} ga oshirildi. Jami: {mavjud['danasi']}.")
        else:
            try:
                yangi_bahasi = int(input("Product bahasi: "))
                yangi_danasi = int(input("Product sani: "))
            except ValueError:
                print("Bahasi hám sani san boliwi kerek!")
                continue
            yangi_code = max((p['code'] for p in products), default=0) + 1
            products.append({
                "code": yangi_code,
                "name": yangi_name,
                "bahasi": yangi_bahasi,
                "danasi": yangi_danasi
            })
            print(f"✅ Jana product qosildi (code: {yangi_code}).")

    elif tanlov == "5":
        basket = []
        total_sum = 0

        print("\n SATIW BOLIMI ")
        while True:
            code = input("\nProduct codeni kiritin (yaki 'exit'): ").lower()
            if code == "exit":
                break

            try:
                code = int(code)
            except:
                print("Code san boliwi kerek!")
                continue

            product = next((p for p in products if p['code'] == code), None)
            if not product:
                print("Bunday code joq!")
                continue

            if product['danasi'] < 1:
                print("Bu product qalmagen!")
                continue

            try:
                miqdor = int(input("Qansha dana?: "))
            except:
                print("Mugdar san bolsın!")
                continue

            if miqdor < 1 or miqdor > product['danasi']:
                print(f"Mumkin mugdar: 1 - {product['danasi']}")
                continue

            basket.append({
                "product": product,
                "danasi": miqdor,
                "jami": miqdor * product['bahasi']
            })
            total_sum += miqdor * product['bahasi']
            print(f"✔ Sebetge qosildi: {product['name']} x {miqdor}")

        if not basket:
            print("Hech narsa tanlanmadi.")
            continue

        savol = input(f"\nUliwma summa: {total_sum} summ. Tolew qilaizba? (awa/yaq): ").lower()
        if savol == "awa":
            print("\n CHEK ")
            vaqt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Sana/Waqit: {vaqt}\n")

            for item in basket:
                product = item["product"]
                danasi = item["danasi"]
                jami = item["jami"]

                product["danasi"] -= danasi

                sales_history.append({
                    "name": product['name'],
                    "bahasi": product['bahasi'],
                    "danasi": danasi,
                    "jami": jami,
                    "vaqt": vaqt
                })

                print(f"{product['name']} | {danasi} dona | {jami} so'm")

            print(f"\nUmumiy: {total_sum} so'm")
            print("Tolew qabillandi ")
        else:
            print(" Productler skladqa qatarildi.")

    elif tanlov == "6":
        if not sales_history:
            print("Ele heshnarse satilmagan.")
            continue

        print("\nESABAT (Satilgan productlar):")
        total_sum = 0
        for s in sales_history:
            print(f"{s['vaqt']} | {s['name']} | Bahasi: {s['bahasi']} | Danasi: {s['danasi']} | Jami: {s['jami']}")
            total_sum += s['jami']

        print(f"\n💰 Uliwma sawda summasi: {total_sum} sum")

    else:
        print("Qate tanlaw. 0 den 6 ge deyin san kiritin.")
