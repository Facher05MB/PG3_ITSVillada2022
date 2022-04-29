class Calculadora():
    def __init__(self,):
        self.resultado=0
        self.numero1=int(input("agrege el segundo numero "))
        self.numero2=int(input("agrege el primer numero "))
        print("\n")
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    
    def sumar(self):
       
        self.resultado = self.numero1 + self.numero2
        print("resultado de suma", self.resultado)

        

    def restar(self):
       
        self.resultado = self.numero1 - self.numero2
        print("resultado de resta", self.resultado)

    def multiplicar(self):
        
        self.resultado=self.numero1 * self.numero2
        print("resultado de multiplicacion", self.resultado)

    def dividir(self):
        try:
            self.resultado = self.numero1 / self.numero2
            print("resultado de dividision", self.resultado)
        except:
            print("cualquie numero dividio por 0 es infinto")


# bloque principal

calculadora1=Calculadora()

