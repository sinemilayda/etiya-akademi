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

studentcount=44
if studentcount>20:
    print("derse devam")

vize=int(input("vize: "))
final=int(input("final:"))
ortalama =(vize*0.4)+(final *0.6)
#final<40 kaldı , ort<50 kaldı, vize finalin 2 katıysa kaldı, diğerlerinde geçti
if vize<40:
    print("kaldı")
elif vize==final*2:
    print("kaldı")
elif ortalama<50:
    print("kaldı")
else:
    print("geçti")

#or and - true false 
if final<40 or ortalama<50 or vize==final*2:
    print("kaldı")
else:
    print("geçti")
    #deneme


#karar yapıları end