import random

print("====EJERCICIO N°4")

def bubble_sort(lista1):  
    for i in range(0,len(lista1)-1):  
        for j in range(len(lista1)-1):  
            if(lista1[j]>lista1[j+1]):  
                temp = lista1[j]  
                lista1[j] = lista1[j+1]  
                lista1[j+1] = temp  
    return lista1  

lista1 = [random.randint(0, 99) for x in range(5)]
print("Generando lista aleatoria...")
print("Tu lista generada sin ordenar: " ,lista1)
print("La lista ordenada: ", bubble_sort(lista1)) 