while True:
    try:
        num1=int(input("Ingrese un número: "))
        num2=int(input("Ingrese un segundo número que sume al primero: "))
        sum=num1+num2
        print("La suma es: ", sum)
        ans=input("si queire terminar presione [0], si desea continuar precione cualquier otra: ")
        if ans=="0":
            break  
    except ValueError:
       print("Porfavor ingrese numeros")