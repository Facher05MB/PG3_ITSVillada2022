
from operator import truediv


print("ejercicio 2")

def bisisesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print (año, " es viciesto")
    else:
        print (año, " no es viciesto")
while True:
  año= int(input("digame el año "))
  bisisesto(año)

 