class Familia():
    def __init__(self, papa, mama, hijos):
        self.papa = papa
        self.mama = mama
        self.hijos = hijos
        self.hijos_list = []

    def añadir_hijos(self, hijo):
        self.hijos_list.append(hijo)

    def __str__(self):
        return "Familia: " + self.name + " hijos: " + self.hijos_list

fami = Familia()
fami.papa = "Curcuru"
fami.mama = "maya"
fami.hijos = "3"
fami.añadir_hijo("Cativa")
fami.añadir_hijo("Lichi")
fami.añadir_hijo("Alejo")
print(fami)
