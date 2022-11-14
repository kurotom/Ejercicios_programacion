#
# Conversor de unidades de temperaturas: Fahrenheit-Celcius
#

print ()
print ("-                                             -")
print ("-----------------------------------------------")
print ("-   Bienvenido a convertidor de temperatura   -")
print ("-----------------------------------------------")
print ("-                                             -")
print ()

while True:
    print ("_______________________________________________")
    print ()
    print ("             ¿Qué desea convertir?             ")
    print ("_______________________________________________")
    print ()
    TE = input ("Celcius (c) o Fahrenheit (f):  ")
    print ()

    if TE == 'c':       # Grados celcius
        print ("Fahrenheit a Celcius")
        X = float (input ("Grados fahrenheit: "))
        XX = float ((X - 32) / 1.8)
        print ()
        print (X,"° fahrenheit son", XX,"° celcius" )
        print ()
    elif TE == 'f':         # Grados fahrenheit
        print ("Celcius a Fahrenheit")
        print ()
        Y = float(input("grados Celcius: "))
        YY = float((Y * 1.8) + 32)
        print ()
        print (Y,"° celcius son",YY,"° fahrenheit")
        print ()
    SAL = input("Quiere salir? s/n: ") # Opción salida del programa
    if SAL == "s":
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print ("!!           Saliendo           !!")    # quiere salir
        print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        break
    elif SAL == "n":
        print ()        # no quiere salir y seguir usando el programa
    else:
        print ("#####################################")
        print ("##  Seleccione parámetros válidos  ##") # Otra opción
        print ("#####################################") # error
        
