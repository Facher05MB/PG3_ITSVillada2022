while True:
    
    try:
        num1 = int(input ("ingrese el primer numero:"))
        num2 = int(input ("ingrese el segundo numero:"))

        r = num1 / num2

        print ("el resultado es:", r)
        menu = int (input ("para terminar precione 0 /// para continuar precione 1: "))

        if menu == 0:
            break



    except (ValueError,):
        print ("ingrese numeros correctamente")
    except ( ZeroDivisionError):
        print ("no se puede dividir por cero")