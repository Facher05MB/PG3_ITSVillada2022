from re import S


class Triangulo():
    
    def __init__(self):
        self.lado1=int(input("agrege el primer lado "))
        self.lado2=int(input("agrege el segundo lado "))
        self.lado3=int(input("agrege el tercer lado "))
        self.equilatero()
        self.lado_mayor()

    def lado_mayor(self):
        if (self.lado1 > self.lado2):
            self.mayor = self.lado1
            if (self.mayor > self.lado3):
                 print("El lado mayor es el lado 1 que mide:", self.mayor)
            else:
                 self.mayor = self.lado3
                 print("el lado mayot es el lado 3 que mide:", self.mayor)
        else:
            self.mayor = self.lado2
            if (self.mayor > self.lado3):
                 print("El lado mayor es el lado 2 que mide:", self.mayor)
            else:
                 self.mayor = self.lado3
                 print("el lado mayor es el lado 3 que mide:", self.mayor)
    def equilatero(self):
        if (self.lado1 == self.lado2  and self.lado2 == self.lado3):
            print("es un triangulo equilatero")
        else:
            print("no es un triangulo equilatero")


#bloque principal

triangulo1=Triangulo()


