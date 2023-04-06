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
