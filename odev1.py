#değişkenler start

baslik = 'Haberiniz olsun'  #integer
vade = 12  #integer
faizOrani = 1.47  #float
print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani))
mesaj = "Hoşgeldin"
musteriAdi = "İlayda"
musteriSoyadi = "Yücel"
sonucMesaj = mesaj + " " + musteriAdi + " " + musteriSoyadi + "!"

print(sonucMesaj)
sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)
print(sonucMesaj)

#değişkenler end

#döngüler start

krediler = [
  "Hızlı Kredi", "Maaşını Halkbanktan Alanlara Özel",
  "Mutlu Emekli İhtiyaç Kredisi"
]
#alias,kod adı
for kredi in krediler:
  print("<option>" + kredi + "<option>")

for i in range(len(krediler)):
  print(krediler[i])
 
for i in range(3, 10):
  print(i)

for i in range(0, 11, 2):
  print(i)
  
#döngüler end

#listeler start

krediler = [ "Hızlı Kredi", "Maaşını Halkbanktan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))  #uzunluk
krediler[0] = "Çabuk Kredi"
print(krediler)
#print(krediler[3])

#listeler end

#sartblokları start

dolarDun = 7.65
dolarBugun = 7.65
if dolarDun > dolarBugun:
  print("Azalış Oku")
  print("Bitti")
elif dolarDun < dolarBugun:
  print("Artış Oku")
else:
  print("Eşittir oku")
print("Bitti")

#if dolarDun<dolarBugun:
#print("Artış Oku")
#if dolarDun==dolarBugun:
#print("Eşittir Oku")

#sartblokları end

#fonksiyonlar start

def kredilerilistele():
  krediler = [
    "Hızlı Kredi", "Maaşını Halkbanktan Alanlara Özel",
    "Mutlu Emekli İhtiyaç Kredisi"
  ]
  for kredi in krediler:
    print("<option>" + kredi + "<option>")


kredilerilistele()
kredilerilistele()
kredilerilistele()

#fonksiyonlar end