while True:
    
    try:
        texto = input("Escriba cualquier texto:  ")
        archivo = open('texto_ejemplo.txt', 'w')

        if texto.isnumeric():
            archivo.write(int(texto))
        else:
            menu = int (input ("para terminar precione 0 /// para continuar precione 1: "))

        if menu == 0:
            break

    except TypeError:
        print("no ingrese numeros")