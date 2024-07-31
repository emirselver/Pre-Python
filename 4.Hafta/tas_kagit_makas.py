import random
import time

def kazanani_belirle(kullanici_secimi, bilgisayar_secimi):

    if kullanici_secimi == bilgisayar_secimi:
        return "Beraberlik!"

    elif (kullanici_secimi == "taş" and bilgisayar_secimi == "makas") or \
         (kullanici_secimi == "makas" and bilgisayar_secimi == "kağıt") or \
         (kullanici_secimi == "kağıt" and bilgisayar_secimi == "taş"):
         return "Kullanıcı Kazandı!"

    else:
        return "Bilgisayar Kazandı!"

def oyunu_baslat():
    secenekler = ["taş", "kağıt", "makas"]
    secim = input("Taş, kağıt, makas? Bir seçenek seçiniz lütfen. (Çıkış yapmak için 'çık' yazmanız yeterli) : ").lower()

    pc_secimi = random.choice(secenekler)

    if secim == "çık":
        print("Çıkış yapılıyor...\n")
        time.sleep(3)
        print("Çıkış yapıldı.")

    elif secim not in secenekler:
        print("Hatalı giriş yaptınız!")

    else:
        sonuc = kazanani_belirle(secim, pc_secimi)
        
        time.sleep(1)
        print(f"Kullanıcının seçimi: {secim}")
        print(f"Bilgisayarın seçimi: {pc_secimi}")
        time.sleep(2)
        print(f"Sonuç: {sonuc}")

oyunu_baslat()
    