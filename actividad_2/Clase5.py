


class Persona():
    def __init__(self) :
        self.Nombre = input("Digame su nombre ")
        self.edad = int(input("Digame su edad "))
        print("Hola ", self.Nombre, " tienes ", self.edad)



class Empleado(Persona):
    def __init__(self): 
        super().__init__()
        self.sueldo = int(input("digame su sueldo "))
        self.impuestos()

    def impuestos(self):

        if(self.sueldo > 3000):
            print("tienes que pagar deudas")
        else:
            print("no tienes deudas")

    

p1=Persona()
p2=Empleado()