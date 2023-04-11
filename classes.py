class Human:
    #property, attribute => özellik, nitelik
    name=""
    age=20

    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("yapıcı blok çalıştı")
    

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