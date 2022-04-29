from re import S


class Triangulo():
    
    def __init__(self):
        self.lado1=int(input("agrege el primer lado "))
        self.lado2=int(input("agrege el segundo lado "))
        self.lado3=int(input("agrege el tercer lado "))
        self.equilatero()
        self.lado_mayor()

    def lado_mayor():
        S


    def equilatero(self):
        if self.lado1 == self.lado2 == self.lado3:
            print("es un triangulo equilatero")
        else:
            print("no es un triangulo equilatero")


#bloque principal

triangulo1=Triangulo()


