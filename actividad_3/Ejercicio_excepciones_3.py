while True:
    try:
        meses = ("Enero", "Febrero", "Marzo", "Abril", 'Mayo', 'Junio', 'Julio'
                ,'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')

        print (meses)

        mesel = int (input("elija el mes segun el numero: "))

        print (meses[mesel - 1])
        menu = int (input ("para terminar precione 0 /// para continuar precione 1: "))
        if menu == 0:
            break

    except (IndexError,ValueError):
        print( "ingres el numero del mes correctamente")