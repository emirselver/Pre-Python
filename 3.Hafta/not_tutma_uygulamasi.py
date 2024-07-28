notlar = []

while True:
    print("")
    print((20 * "*") + (" NOT UYGULAMASI ") + (20 * "*"))
    print("1. Not Ekleme")
    print("2. Notları Görüntüle")
    print("3. Not Güncelleme")
    print("4. Not Silme")
    print("5. Çıkış Yap\n")

    secim = int(input("İşlem Yapmak İstediğiniz Menüyü Seçiniz: "))

    if secim == 1:
        baslik = input("\nNot Başlığı Giriniz: ")
        icerik = input("Not İçeriği Giriniz: ")

        not_ekle = {"Başlık" : baslik , "İçerik" : icerik}
        notlar.append(not_ekle)

        print("\nNot başarılı bir şekilde eklendi!")

    elif secim == 2:

        if len(notlar) == 0:
            print("Henüz Not Eklemediniz!")

        else:
            index = 0
            for _ in notlar:
                not_basligi = notlar[index]["Başlık"]
                not_sirasi = index + 1
                print(f"{not_sirasi}. {not_basligi}")
                index += 1

            icerik_goruntule = int(input("\nİçeriğini Görüntülemek İstediğiniz Notu Giriniz: "))

            if 0 >= icerik_goruntule > len(notlar):
                print("\nListede Olmayan Not Seçtiniz!")

            not_baslik = notlar[icerik_goruntule - 1]["Başlık"]
            not_icerigi = notlar[icerik_goruntule - 1]["İçerik"]
        
            print(f"Başlık: {not_baslik} ")
            print(f"İçerik: {not_icerigi} ")

    elif secim == 3:
        index = 0
        for _ in notlar:
             not_basligi = notlar[index]["Başlık"]
             not_sirasi = index + 1
             print(f"{not_sirasi}. {not_basligi}")
             index += 1


        not_guncelle = int(input("Güncellemek İstediğiniz Notu Seçiniz: "))

        if 0 >= not_guncelle > len(notlar):
            print("Listede Olmayan Not Seçtiniz!")

        yeni_baslik = input("Yeni Başlık Giriniz: ")
        yeni_icerik = input("Yeni İçerik Giriniz: ")

        notlar[not_guncelle - 1]["Başlık"] = yeni_baslik
        notlar[not_guncelle - 1]["İçerik"] = yeni_icerik

        print("Not Başarıyla Güncellendi...")

    elif secim == 4:
        if len(notlar) == 0:
            print("Henüz Not Eklemediniz!")
        
        else:
            index = 0
            for _ in notlar:
                not_basligi = notlar[index]["Başlık"]
                not_sirasi = index + 1
                print(f"{not_sirasi}. {not_basligi}")
                index += 1

            not_sil = int(input("Silmek İstediğiniz Notu Giriniz: "))

            if not_sil > len(notlar) or not_sil <= 0:
                print("Listede Olmayan Not Seçtiniz!")
        
            else:
                notlar.pop(not_sil - 1)
                print("Not Silme İşlemi Başarıyla Gerçekleşti...")
            
    
    elif secim == 5:
        print("Program sonlandırılıyor...")
        break

    else:
        print("Hatalı İşlem Yaptınız!")





