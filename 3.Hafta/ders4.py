#Döngülerde bahsedilecek kavramlar:
#----> -range (len), break, continue

#YAPILACAK ÖRNEK UYGULAMALAR:
#1) Girilen sayının tek mi çift mi olduğunu bulan program
#2) Kullanıcı Giriş İşlemi (3 Haklı)
#3) Faktöriyel Hesaplama
#4) Çarpım tablosu (iç içe döngüler)
#5) Listedeki tek çift elemanları toplayıp teklerin toplamına bölme (listeye 5 eleman döngüyle alınacak)
#6) Basit ATM Simülasyonu

#-------------Akış/Algoritma şemasından bahsedilecek-------------

#7) Asal Sayı Bulma
#8) Fibonacci Dizisi
#9) Listedeki En Büyük Elemanı Bulma
#10) Klavyeden girilen sayının mükemmel sayı olup olmadığını bulan program (Kendisi hariç bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara mükemmel sayı denir)
#11) Girilen sayinin Güçlü sayi olup olmadığını söyleyen program Not: rakamları çarpımı ile rakamları toplamının toplamı kendine eşit olan iki basamaklı sayılara denir
#12) 10 elemanlı bir sayı dizisinde en küçük elemanın bu dizinin kaçıncı elemanı olduğunu bulan program
#13) Sayı tahmin oyunu (ipuculu/belki random modülü anlatılabilir)

#1) Girilen sayının tek mi çift mi olduğunu bulan program:

# sayi = int(input("Sayi giriniz: "))
# if sayi % 2 == 0:
#     print("sayi çift")
# else:
#     print("sayi negatif")

#------------------------------------------##------------------------------------------#

#2) Kullanıcı Giriş İşlemi (3 Haklı)

# kullanici_adi = "admin"
# sifre = "admin123"

# sayac = 0

# while sayac < 3:
#     sayac += 1

#     kAdi = input("Kullanici adi giriniz: ")
#     kSifre = input("Sifre giriniz: ")

#     if kAdi == kullanici_adi and kSifre == sifre:
#         print("Giris islemi basarili...")
    
#     elif sayac == 3:
#         print("Giris hakkiniz kalmadi!")
#         break

#     else:
#         print((3 - sayac), "hakkiniz kaldi")

#------------------------------------------##------------------------------------------#

#3) Faktöriyel Hesaplama

# faktoriyel = int(input("Faktoriyelini hesaplamak istediginiz sayiyi giriniz: "))
# toplam = 1

# for i in range(1, faktoriyel + 1):
#     toplam *= i

# print(f"{faktoriyel}! işleminin sonucu: {toplam}")

#------------------------------------------##------------------------------------------#

#4) Çarpım tablosu (iç içe döngüler)

# for i in range(1, 10):
#     for j in range(1, 10):
#         carpim = i * j
#         print(f"{i} x {j} = {carpim}")

#------------------------------------------##------------------------------------------#

#5) Listedeki tek çift elemanları toplayıp teklerin toplamına bölme (listeye 5 eleman döngüyle alınacak)

# sayilar = []
# cift_toplam = 0
# tek_toplam = 0

# kac_eleman = int(input("Kac eleman girmek istiyorsunuz? : "))
# for i in range(1, kac_eleman + 1):
#     sayi = int(input(f"{i}. Sayiyi Giriniz: "))
#     sayilar.append(sayi)

#     sayilar_uzunluk = len(sayilar)

# for sayi in sayilar:
#     if sayi % 2 == 0:
#         cift_toplam += sayi
#     else:
#         tek_toplam += sayi

# bolum = cift_toplam / tek_toplam
# if bolum == 0:
#     print("Bolme islemi yapilamadi...")

# print("Listedeki cift sayilarin tek sayilar toplamına bölümü :{} ".format(bolum))

#------------------------------------------##------------------------------------------#

#6) Basit ATM Simülasyonu

# bakiye = 100

# while True:

#     print("1) Bakiye Sorgula")
#     print("2) Para Yatir")
#     print("3) Para Cek")
#     print("4) Cikis Yap\n")
    
#     secim = int(input("Lutfen yapmak istediginiz islemi tuslayiniz: "))

#     if secim == 1:
#         print(f"Guncel Bakiyeniz: {bakiye} TL\n")

#     elif secim == 2:
#         yatirilan_tutar = int(input(f"Yatirmak istediginiz tutari giriniz: (Guncel bakiye: {bakiye} TL)\n "))
#         bakiye += yatirilan_tutar
#         print("Para yatirma islemi basarili. Guncel bakiyeniz: {} TL\n".format(bakiye))

#     elif secim == 3:
#         cekilen_tutar = int(input(f"Lutfen cekmek istediginiz para tutarini giriniz: (Guncel bakiye: {bakiye} TL)\n"))
#         if cekilen_tutar > bakiye:
#             print("Limit asimi! İslem yapilamiyor... Lutfen tekrar deneyiniz.\n")
#         else:
#             bakiye -= cekilen_tutar
#             print("Para cekme islemi basarili. Guncel bakiyeniz: {} TL\n".format(bakiye))
    
#     elif secim == 4:
#         print("Oturum sonlandiriliyor...\n")
#         break

#     else:
#         print("Hatali islem yaptiniz!")
        
    

