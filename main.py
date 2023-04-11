print("Merhaba Etiya")
print("etiya")
#yorum satırı
#değişkenler start

#string
text="merhaba" #çift tırnak metinsel değeri temsil eder.
print(text)
print(text)
text="selam"
print(text)
print(text)

studentcount=45 #sayı olduğu için tırnak kullanmadık int,tam sayı
print(studentcount +5)
averagepoint=25.5 #double,decimal,float, ondalıklı sayı
print(averagepoint)
isverified= True #bool, boolean, True veya False
print(isverified)
print(type(text))
print(type(studentcount))
print(type(averagepoint))
print(type(isverified))
#değişkenler end

#operatörler start
number=10
#matematiksel operatörler 
print(number+number)
print(number-5)
print(number/2) #bölüm sonucunu float türünde verir. tam bölünse dahi.
print(number*5)
print(number%2) #mod operatörü sol taraftaki değerin sağ taraftaki değere bölümünden kalan
#mantıksal operatörler geri dönüş türü boolean 
print(number==10) #True verir sayımız 10
print(10!=10)#false burda 10 10 eşit değildir diyor.
print(11!=10)#true
print(number > 10)#false
print(number >= 10)#true
print(number < 10)#false
print(number <= 10)#true
#operatörler end


#diziler listeler start
print("*************************")
sayilar=[100,200,300,"merhaba",15.5,True]#listedeki tüm elemanların veri tipi aynı olmak zorunda değil
#saymaya 0 dan başlıyoruz, index
print(sayilar)
print(sayilar[0])

print(sayilar)
sayilar.append(100)#listenin sonuna 600 ekliyor
sayilar.append(600)
print(sayilar)
sayilar.pop()#verilen indexi atıyor. indexe göre çalışır indexteki elemanı siler(default son index)
print(sayilar)
sayilar.remove(100)#parantez içine yazılan ilk veriyi siler.
print(sayilar)
sayilar.extend([700,800,900])#toplu liste eklemesi, append'in aksine tek bir değer atamaz
print(sayilar)
sayilar.clear()#dizinin tamamını temizliyor.
print(sayilar)
#diziler listeler end

#string interpolation start
hello="Merhaba"
userName= "İlayda"
totaltext=hello+" "+userName
print(totaltext)

totaltext= "{message} Sayın {name}".format(message=hello, name=userName)
print(totaltext)

#f-string
totaltext= f"hoşgeldin {userName}" #otomatik formatlıyor.
print(totaltext)
#string interpolation end

#karar yapıları start
#ortalamanot=input("ortalamanı yaz: ")

#numerik int, double
#type conversion start
#ortalamanotasint = int(ortalamanot)
#type conversion end

#4 satır 1 tab/indent
#if else
#if ortalamanotasint >80:
   # print("geçtiniz")
  #  if ortalamanotasint >80:
   #     print("başarılı")
#else if= elif
#elif ortalamanotasint >50:
 #   print("az başarılı")
#elif ortalamanotasint >60:
 #   print("orta başarılı")
#else:
 #   print("kaldın")

# studentcount=44
# if studentcount>20:
#     print("derse devam")

# vize=int(input("vize: "))
# final=int(input("final:"))
# ortalama =(vize*0.4)+(final *0.6)
# #final<40 kaldı , ort<50 kaldı, vize finalin 2 katıysa kaldı, diğerlerinde geçti
# if vize<40:
#     print("kaldı")
# elif vize==final*2:
#     print("kaldı")
# elif ortalama<50:
#     print("kaldı")
# else:
#     print("geçti")

# #or and - true false 
# if final<40 or ortalama<50 or vize==final*2:
#     print("kaldı")
# else:
#     print("geçti")
#     #deneme

# sayi=[]
# for i in range(3):
#     sayi.append(int(input(f"{i+1}.sayı:")))
# sayi.sort() #sort küçükten büyüğe sıralıyor eğer içine reverse=true dersek tam tersi sıralar
# buyuk=int(input("kaçıncı: "))
# print(sayi[buyuk-1])
# for i in range(0,forRange+1,2):
#     print(i)

# rmin=int(input("alt:"))
# rmax=int(input("üst:"))
# for i in range(rmin,rmax):
#     if i%2==0:
#         print(i)
#karar yapıları end ctrl ö yorum yada 3 tırnak

#döngüler start
for i in range(0,10):
    print(i)
ogranci=["v","s","z","i","ü"]
#length
print(len(ogranci))

for i in range(len(ogranci)):
    #if i>3:
     #   break #looptan çıkıyor
    if i==3:
        pass #ilgili alanın bodysini boş bırakıyor.
    print(f"{i+1}.Öğrenci: {ogranci[i]}")
for i in range(0,10):
    pass

for i in ogranci:
    if i=="v":
        continue #o değeri atlayıp diğer değerleri yazıyor.
    print(f"öğrenci: {i}")
#yada
for i in ogranci:
    print(f"Öğrenci: {i}")

#while boolean
# while True:
#     print("merhaba") #sonsuz döngü ctrl c terminal durdurur.
i=0
while i<10:
      i=i+1
      if i==3:
          break
      print(f"while içindeki i değeri: {i}")
#döngüler end
#fonksiyonlar start
def ortalamaHesapla() -> None:
    final=100
    vize=100
    ort=(vize*0.4)+(final*0.6)
    print(ort)
def ortalamahesaplavedondur(vize:float, final:float) -> float: #geriye float dönecek diyoruz.
    return (vize*0.4)+(final*0.6)
    
#geriye döndürmek
ortalamaHesapla()
benimort2= ortalamaHesapla() #none değeri
print(ortalamahesaplavedondur(70,100))
print(benimort2)
#triggerlamak, çalıştırmak, execute etmek
#fonksiyonlar end
#class ,nesne, obje start
class Human:
    #property, attribute => özellik, nitelik
    name=""
    age=20

    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("yapici blok çalişti")
    

    #davranışlar
    def talk(self, message):
        print(f"{self.name}: {message}")

    def walk(self):
        print(f"{self.name} is walking..")

human1=Human()#constructor => yapıcı blok
human1.name="İlayda"
human1.age=25
human1.talk("merhaba")
human1.walk()
#class end