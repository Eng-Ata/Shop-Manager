mahsulat = []            
hazineh = []
saham = []
moshtarian = []
forosh = []

def ez_mahsulat():
    name = input("نام محصول را وارد کن: ")
    hazine = int(input("قیمت محصول را وارد کن: "))
    saham = int(input("موجودی محصول را وارد کن: "))
    mahsulat.append(name)
    hazineh.append(hazine)
    saham.append(saham)
    print(f"محصول {name} اضافه شد.")

def ez_moshtarian():
    name = input("نام مشتری را وارد کن: ")
    phone = input("شماره مشتری را وارد کن: ")
    moshtarian.append({"name": name, "phone": phone})
    print(f"مشتری {name} اضافه شد")

def fr_mahsulat():
    print("\nلیست کالاها:")
    for i in range(len(mahsulat)):
        print(f"{i + 1}. {mahsulat[i]} - قیمت: {hazineh[i]} تومان، موجودی: {saham[i]}")

    ch = int(input("\nشماره کالا را وارد کن: ")) - 1
    q = int(input("تعداد فروش را وارد کن: "))
    saham[ch] -= q
    print(f"{q} عدد از {mahsulat[ch]} فروخته شد.")

def record_fr():
    print("\nلیست کالاها:")
    for i in range(len(mahsulat)):
        print(f"{i + 1}. {mahsulat[i]} - قیمت: {hazineh[i]} تومان")

    tp = 0
    items = input("\nشماره کالاهای فروخته‌شده را جدا کنید (مثلاً: 1,2): ").split(",")
    si = []

    for item in items:
        index = int(item.strip()) - 1
        quantity = int(input(f"تعداد {mahsulat[index]}: "))
        saham[index] -= quantity
        tp += quantity * hazineh[index]
        si.append((mahsulat[index], quantity))

    print("\nصورت‌حساب:")
    for name, quantity in si:
        print(f"{name} - تعداد: {quantity}")
    print(f"مبلغ کل: {tp} تومان")

    forosh.append({"items": si, "total": tp})
    print(" ثبت شد.")

def main():
    while True:
        print("\n--- سیستم مدیریت فروش ---")
        print("1 افزودن کالا")
        print("2 افزودن مشتری")
        print("3 فروش کالا")
        print("4 ثبت صورت‌حساب")
        print("5 خروج")

        choice = input("انتخاب کن: ")

        if choice == "1":
            ez_mahsulat()
        elif choice == "2":
            ez_moshtarian()
        elif choice == "3":
            fr_mahsulat()
        elif choice == "4":
            record_fr()
        elif choice == "5":
            print("خروج")
            break
        else:
            print("انتخاب نامعتبر است")

main()
