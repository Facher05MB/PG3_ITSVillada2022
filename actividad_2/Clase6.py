from audioop import add


class Familia():
    def __init__(self):
        self.Padre = input("nombre del padre ")
        self.Madre = input("nombre de la madre ")
        self.numelista = int(input("cuantos hijos tines "))
        self.hijos = []
        self.numero_hijo = int(0)
        if (self.numelista > self.numero_hijo):
            self.nombrehijo = input("escriba el nombre de tu hijo n°", self.numero_hijo)
            self.hijos.append(self.nombrehijo)
            self.numero_hijo = self.numero_hijo + 1
            print(self.hijos)


hijos = list()
F1=Familia()