#LİSTELER

# -> Liste oluşturma:
sehirler = ["istanbul","ankara","bursa","adana"]
print(sehirler)

# -> Listenin eleman sayısını bulma:
print(len(sehirler))

# -> Listedeki herhangibir elemana erişöe:
sehirler[2]
sehirler[-1] #Tersten erişim sağlar.
sehirler[::-1] #Elemanları tersten yazdırır.

# -> Liste parçalama:
sehirler[0:2]
sehirler[::2]

# -> Liste içinde farklı liste tanımlama:
sehirler_ilceler = ["Karaköprü","Haliliye",sehirler,["Türkiye","Almanya"]]

# -> Liste içindeki bir başka listenin elemanına erişme:
sehirler_ilceler[3][1]

# -> Liste elemanlarını güncelleme:
sehirler[1] = "Şanlıurfa"

# -> Liste üzerine yeni değerler ekleme:
yeni_liste = sehirler + ["Trabzon","Kocaeli"]

# -> append() metodu: Listenin sonuna yeni eleman ekler:
sehirler.append("Aydın")

# -> insert() metodu: Listede belirlediğimiz indexe yeni eleman ekler:
sehirler.insert(0, "Kütahya")

# -> extend() metodu: Listeye verdiğimiz değerleri eleman olarak ekler:
ulkeler = ["Türkiye","Almanya"]
sehirler.extend(ulkeler)

# -> remove() metodu: Listeden eleman silmeye yarar:
sehirler.remove("Şanlıurfa")

# -> pop() metodu: Listedeki son elemanı siler ve gösterir:
silinen_deger = sehirler.pop()
silinen_deger = sehirler.pop(3) #index belirterek de kullanabiliriz.

# -> del() metodu: Listedeki herhangi bir index numarasındaki elemanı siler:
del sehirler[3]
del sehirler # ----> Eğer index numarası vermezsek listeyi olduğu gibi siler.


# -> reverse() metodu: Listeyi ters çevirir:
sehirler.reverse()

# -> sort() metodu: Listeyi içindeki değere göre (alfabetik, sayı) sıralar:
sehirler.sort() #Alfabetik olarak sıralayacak.
sehirler.sort(reverse = True) #Tersten sıralar.

# -> copy() metodu: Listedeyi kopyalar : List bir class ve bellekte referans tip olarak ele alınır dolayısıyla bir listeyi başka bir listeye atamak istediğimizde liste elamanları kopyalanmaz bunun yerine listenin bellekteki adres bilgisi kopyalanır. a = ["apple","banana"]
# b = ["grape","cherry"]
# a = b
# Burada b'nin adresi a listesine atanmıştır. Dolayısıyla artık a ve b listeleri belleğin aynı adresindeki aynı verilere sahiptir. (["grape","cherry"])

# Dolayısıyla a ya da b üzerinde yaptığımız her hangi bir değişiklik iki liste üzerinde de yapılmış olur. 


# -> min() metodu: Listedeki en küçük elemanı bulur (alfabetik de olabilir) :
sayilar = [2,25,46,48,7,123]
print(min(sayilar))

# -> max() metodu: Listedeki en büyük elemanı bulur (alfabetik de olabilir):
sayilar = [2,25,46,48,7,123]
print(max(sayilar))

# -> sum() metodu: Listedeki elemanları toplar (int destekler):
print(sum(sayilar))

# -> Döngü kullanarak listedeki elemanları yazdırma:

for sayi in sayilar:
    print(sayi)

# -> in keywordu kullanımı:
sayi2 = 15
print(sayi2 in sayilar)

# -> join() metodu: Listedeki elemanları birleştirir (listeyi - stringe çevirme):
string_sehirler = ",".join(sehirler) #Tırnak içine ne ile ayırmak istiyorsak onu yazıyoruz
print(string_sehirler)


# -> split() metodu: Verdiğimiz karaktere göre stringi ayırır:
ayirma = string_sehirler.split(",")
print(ayirma)

#--------------------------------------------------------------------#--------------------------------------------------------------------#

#DEMET (TUPLE)

#Listelerin neredeyse aynısı, eleman erişimi, döngü ile yazdırma vs...
#Farkları neler peki?
#----> -Elemanları güncellenemez, silinemez (append, remove vs.yok)

sayi_demeti = (1,8,44,15,32,78,15,645)

# -> count() metodu: Tuple içerisindeki tekrarlayan elemanların sayısını verir.
sayi_demeti.count(15)

# -> index() metodu: Tuple içerisindeki bir elemanın index numarasını verir.
sayi_demeti.index(8)

#--------------------------------------------------------------------#--------------------------------------------------------------------#

#KÜME (SET)
#Kümede bir eleman sadece bir kez bulunabilir. Elemanlar sıralanamaz, dolayısıyla set'e eklediğimiz bir elemanın hangi sırada olduğunu bilemeyiz.

#Küme (set) oluşturma:
meyveler = {"Elma", "Portakal", "Kiraz"}
for meyve in meyveler:
    print(meyve)
    #Herhangibir sıralama olmadığı için her çalıştırdığımızda farklı bir sırayla yazdıracak.

#indexleme olmadığı için set elemanlarına direkt erişemeyiz.

# -> in keywordu kullanımı:
print("Üzüm" in meyveler)

#Kümelerde eleman güncelleyemeyiz ancak yeni eleman ekleyebiliriz:

# -> add() metodu: küme listesine tek bir eleman ekler :
meyveler.add("Şeftali")

# -> update() metodu: küme listesine birden fazla eleman ekler:
meyveler.update(["Mango", "Karpuz"])

# -> remove() metodu: kümeden eleman siler:
meyveler.remove("Mango")
#eğer verdiğim değer kümede yoksa hata verecektir.

# -> discard() metodu: remove() metodundan farklı olarak silmek istediğimiz eleman kümede yoksa hata vermeyecektir.:
meyveler.discard("Vişne")
# -> intersection() metodu: iki kümenin kesişimini verir:

kume1 = {1,5,6,8,12,45}
kume2 = {8,9,12,36,45,54,76}
print(kume1.intersection(kume2))

# -> union() metodu: iki kümenin birleşimini verir:
print(kume1.union(kume2))

#Kümelerin en büyük özelliği: Bir eleman sadece bir defa bulunur...abs

# -> difference() metodu: iki kümenin farkını verir:
print(kume1.difference(kume2)) #kume1 de olup kume2 de olmayan değerleri verir.

# -> in keywordu kullanımı:
print(6 in kume1.union(kume2))

mesaj = set("Merhaba")
print(mesaj)

#--------------------------------------------------------------------#--------------------------------------------------------------------#

#SÖZLÜK (DICTIONARY)