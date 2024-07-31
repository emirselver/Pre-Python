# #Fonksiyonlar
# def selamla():
#     print("hello world")

# #-> fonksiyonda parametre alma durumu:
# def isim_selamla(isim):
#     print("Merhaba ", isim)

# #-> örnek:
# def kare_al(sayi):
#     sonuc = sayi ** 2
#     print(sonuc)

# #-> parametreye varsayılan değer atama:
# def carpma(sayi1, sayi2 = 1):
#     carpim = sayi1 * sayi2
#     print(f"Sonuç: {carpim}")

# #-> fonksiyonlarda çıktıyı kullanmaya çalışma (return kullanmadığımız için hata alacağız bir sonrakinde return önemine işaret etmek için önce böyle bir kullanım yapmayı tercih ettik.):
# def indirim_hesapla(fiyat, indirim_tutari):
#     indirimli_fiyat = fiyat - (fiyat * indirim_tutari / 100)
#     print("İndirimli Fiyat: {}".format(indirimli_fiyat))
    
# yeniden_hesapla = indirim_hesapla(500,25) * 2 #-> hata alacağız
# print(yeniden_hesapla)

# #-> return kullanımı:
# def selamla_return(ad):
#     return f"Merhaba {ad}!"

# print(selamla_return(ad=ahmet)) 

# #-> return kullanımı (örnek): 
# def ehliyet_yas_hesapla(yas):
#     if yas >= 18:
#         return True
#     else:
#         return False

# yas_bilgisi = int(input("Yaşınızı giriniz:"))

# if ehliyet_yas_hesapla(yas = yas_bilgisi) == True:
#     print("Yaşınız ehliyet almaya uygun.")

# else:
#     print(f"{18 - yas_bilgisi} yıl sonra ehliyet alabilirsiniz.")

#-> Kullanıcının tc bilgisine göre maaş çekebilme durumunun gösteren örnek:
import random

def gun_belirle(tc):
    tc_son_hanesi = int(tc[-1])

    if tc_son_hanesi % 2 == 0:
        return "Pazartesi"
    elif tc_son_hanesi % 2 == 1:
        return "Salı"
    else:
        return False

def maas_gunu():
    gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
    odeme_gunu = random.choice(gunler)
    tc_bilgisi = input("T.C Bilgisi Giriniz: ")
    odeme_alma_gunu = gun_belirle(tc=tc_bilgisi)

    if odeme_alma_gunu == False:
        print("Hatalı işlem yaptınız!")

    elif odeme_alma_gunu == odeme_gunu:
        print(f"Gün Bilgisi: {odeme_gunu}")
        print(f"Maaş Gününüz: {odeme_alma_gunu}\n")
        print("Maaşınızı çekebilirsiniz...")
    else:
        print(f"Bugün {odeme_gunu}, sizin Ödeme gününüz {odeme_alma_gunu}")

maas_gunu()


#-> fonksiyonlarda pass kullanımı:

def ornek():
    pass

#Kullanıcı klavyeden "q" harfine basana kadar listeye eleman eklesin, daha sonra en büyük eleman ekrana yazdırılsın:

def en_buyuk_eleman_bul():
    pass

def sayilari_al():
    sayilar = []
    while True:
        pass
