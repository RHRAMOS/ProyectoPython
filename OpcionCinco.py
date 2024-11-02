import math
def opcion_5():
    while True:
     print ("Funciones de constantes")
     print ("1. math.pi: ")
     print ("2. math.e: ")
     print ("3. math.tau: ")
     print ("4. math.inf: ")
     print ("5. math.nan: ")
     print ("6. SALIR")
     opcion = input("Selecciona la operación que deseas realizar: ")
     
     if opcion == '1':
        x = math.pi
        print("Constante π (3.141592...).", x)
     elif opcion == '2':
        x = math.e
        print(f"Constante e (2.71828...), la base de los logaritmos naturales {x}")
     elif opcion == '3':
        x = math.tau
        print(f"Constante τ (2π), la relación entre la circunferencia de un círculo y su radio. {x}")
     elif opcion == '4':
        x = math.inf 
        print(f"Representa el valor infinito positivo{x}")
     elif opcion == '5':
        x = math.nan
        print(x)
     elif opcion == '6':
        break 
    else: 
        print ("Opcion no valida")