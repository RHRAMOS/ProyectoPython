import math
def opcion_6():
    while True:
        print ("Otras funciones avanzadas ")
        print ("1. math.degrees(x) ")
        print ("2. math.radians(x): ")
        print ("3. math.dist(p, q): " )
        print ("4. math.erf(x): " )
        print ("5. math.erfc(x): " )
        print ("6. math.gamma(x): " )
        print ("7. math.lgamma(x): " )
        print ("8. SALIR " )
        opcion = input("Selecciona la operación que deseas realizar: ")
     
        if opcion =='1':
            x = math.degrees(12)
            print("Convierte un ángulo de radianes a grados.", x)
        elif opcion =='2':
            x = math.radians(8)
            print("Convierte un ángulo de grados a radianes.", x)
        elif opcion =='3':
            x = math.dist((5.1, 9.2), (0, 0))
            print("Devuelve la distancia entre los puntos p y q.",x)
        elif opcion =='4':
            x = math.erf(9)
            print("Devuelve la función de error gaussiana de x.", x)
        elif opcion =='5':
            x = math.erfc(3)
            print(f"Devuelve la función complementaria de error de x. {x}")
        elif opcion =='6':
            x = math.gamma(25)
            print("Devuelve la función gamma de x.", x)
        elif opcion =='7':
            x = math.lgamma(85)
            print(x)
        elif opcion =='8':
             break