#classes.py içindeki humanı kullan
# import classes => tüm classes modülünü import eder.
import random #hazır modül
from classes import Human #=>classes modülünden humanı import
#import openpyxl
#alias => takma ad
#from classes import Human as Insan
#import classes as classlarim
human1=Human("ilayda",23)
human1.talk("selam")

print(random.random()) #random sayı alma