def par_impar():
    print ("funcion para calcular par o impar")

    while True:
        try:
            numero_a_convertir= int(input("ingresa un numero entero"))
            break
        except Exception as err:
            print("Ingresaste un numero inciorrecto")
            print(err)
    
    par_impar = numero_a_convertir % 2

    if par_impar == 0:
        print ("numero par")
    else:
       print("numero impar")
    
    