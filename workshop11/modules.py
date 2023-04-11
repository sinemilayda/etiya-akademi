#alias = takma ad
# import matematik as m --- matematik modülünü import ediyor
from workshop11.matematik import topla as toplamaİslemi # Sadece matematik modülünün içindeki topla fonksiyonunu import ediyor
from workshop11.workshop11 import Human # workshop11 in içindeki Human classını tanıyor.

#built-in modules

import random #python içindeki random modülünü import etti

print(toplamaİslemi(10,20))

print(random.randint(0,100)) # 0 - 100 arası rastgele sayı üretiyor.

Human1 = Human("Mirza")
Human1.talk("Merhaba")