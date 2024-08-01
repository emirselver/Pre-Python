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
# import random

# def gun_belirle(tc):
#     tc_son_hanesi = int(tc[-1])

#     if tc_son_hanesi % 2 == 0:
#         return "Pazartesi"
#     elif tc_son_hanesi % 2 == 1:
#         return "Salı"
#     else:
#         return False

# def maas_gunu():
#     gunler = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma"]
#     odeme_gunu = random.choice(gunler)
#     tc_bilgisi = input("T.C Bilgisi Giriniz: ")
#     odeme_alma_gunu = gun_belirle(tc=tc_bilgisi)

#     if odeme_alma_gunu == False:
#         print("Hatalı işlem yaptınız!")

#     elif odeme_alma_gunu == odeme_gunu:
#         print(f"Gün Bilgisi: {odeme_gunu}")
#         print(f"Maaş Gününüz: {odeme_alma_gunu}\n")
#         print("Maaşınızı çekebilirsiniz...")
#     else:
#         print(f"Bugün {odeme_gunu}, sizin Ödeme gününüz {odeme_alma_gunu}")

# maas_gunu()

# a = 5
# b = 10
# assert a + b == 15
#-> fonksiyonlarda pass kullanımı:

# def ornek():
#     pass

#--------------------------------------# TRY - EXCEPT (HATA YÖNETİMİ) #--------------------------------------#

# -*- coding: utf-8 -*-
"""
Hata Yönetimi (Exception Handling) - Eğitim Dosyası
---------------------------------------------------

Bu dosya, Python'da hata yönetimi ve `try`-`except` bloklarının nasıl kullanılacağını öğretmek için hazırlanmıştır. 
Aşağıdaki örnekler ve açıklamalar, çeşitli hata türlerini nasıl yakalayacağınızı ve yönetebileceğinizi göstermektedir.

1. Basit Hata Yakalama
2. Birden Fazla `except` Bloğu
3. `else` ve `finally` Blokları
4. Kendi İstisnalarınızı Tanımlama
5. Hata Yönetimi Uygulamaları

"""

# 1. Basit Hata Yakalama
def basit_hata_yakalama():
    print("1. Basit Hata Yakalama")
    try:
        sayı = 10 / 0  # Sıfıra bölme hatası
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme hatası!")

# 2. Birden Fazla `except` Bloğu
def birden_fazla_except():
    print("\n2. Birden Fazla `except` Bloğu")
    try:
        sayı = int(input("Bir sayı girin: "))
        sonuç = 10 / sayı
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme hatası!")
    except ValueError:
        print("Hata: Geçersiz giriş! Lütfen bir sayı girin.")

# 3. `else` ve `finally` Blokları
def else_ve_finally():
    print("\n3. `else` ve `finally` Blokları")
    try:
        sayı = int(input("Bir sayı girin: "))
        sonuç = 10 / sayı
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme hatası!")
    except ValueError:
        print("Hata: Geçersiz giriş! Lütfen bir sayı girin.")
    else:
        print(f"Sonuç: {sonuç}")
    finally:
        print("İşlem tamamlandı.")

# 4. Kendi İstisnalarınızı Tanımlama
class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def kendi_istisna_tanimlama():
    print("\n4. Kendi İstisnalarınızı Tanımlama")
    try:
        raise CustomError("Bu özel bir hata mesajıdır.")
    except CustomError as e:
        print(f"Özel Hata: {e}")

# 5. Hata Yönetimi Uygulamaları
def hata_yonetimi_uygulamalari():
    print("\n5. Hata Yönetimi Uygulamaları")
    # Dosya okuma
    try:
        with open('dosya.txt', 'r') as file:
            içerik = file.read()
        print("Dosya içeriği:", içerik)
    except FileNotFoundError:
        print("Hata: Dosya bulunamadı.")
    except IOError:
        print("Hata: Dosya okunurken bir hata oluştu.")
    finally:
        print("Dosya okuma işlemi tamamlandı.")

    # Kullanıcı girişi doğrulama
    while True:
        try:
            yaş = int(input("Yaşınızı girin: "))
            if yaş < 0:
                raise ValueError("Yaş negatif olamaz.")
            print(f"Yaşınız: {yaş}")
            break
        except ValueError as e:
            print(f"Hata: {e}")
            print("Lütfen geçerli bir sayı girin.")

if __name__ == "__main__":
    basit_hata_yakalama()
    birden_fazla_except()
    else_ve_finally()
    kendi_istisna_tanimlama()
    hata_yonetimi_uygulamalari()






#Kullanıcı klavyeden "q" harfine basana kadar listeye eleman eklesin, daha sonra en büyük eleman ekrana yazdırılsın:

# def en_buyuk_eleman_bul(sayilar):
#     if len(sayilar) == 0:
#         return "Listede eleman yok!"

#     en_buyuk_sayi = sayilar[0]  # İlk elemanı en büyük olarak varsay
#     for sayi in sayilar:
#         if sayi > en_buyuk_sayi:
#             en_buyuk_sayi = sayi

#     return en_buyuk_sayi

# def sayi_ekle():
#     sayilar = []
#     while True:
#         girdi = input("Lütfen bir sayı girin (Çıkmak için 'q' tuşuna basın): ")
#         if girdi == 'q':
#             break
#         try:
#             sayi = int(girdi)
#             sayilar.append(sayi)
#         except ValueError:
#             print("Geçerli bir sayı giriniz.")
    
#     return sayilar

# sayilar = sayi_ekle()
# sonuc = en_buyuk_eleman_bul(sayilar)
# print("En büyük sayı:", sonuc)

        
