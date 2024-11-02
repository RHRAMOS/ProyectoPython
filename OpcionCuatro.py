import math
def opcion_4():
   while True:
    print("Funciones hiperbólicas ")
    print("1. math.sinh(x): " )
    print("2. math.cosh(x): " )
    print("3. math.tanh(x): " )
    print("4. math.asinh(x): " )
    print("5. math.acosh(x): " )
    print("6. math.atanh(x): " )
    print("7. SALIR" )
    opcion = input("Selecciona la operación que deseas realizar: ")
    
    if opcion == '1':
        x = math.sinh(25)
        print(" Devuelve el seno hiperbólico de x.", x)
    elif opcion == '2':
        x = math.cosh(12)
        print("Devuelve el coseno hiperbólico de x.",x)
    elif opcion == '3':
        x = math.tanh(52)
        print("Devuelve la tangente hiperbólica de x.",x)
    elif opcion == '4':
        x = math.asinh(9)
        print("Devuelve el arco seno hiperbólico de x.", x)
    elif opcion == '5':
        x = math.acosh(25)
        print("Devuelve el arco coseno hiperbólico de x.",x)
    elif opcion == '6':
        x = math.atanh(0.5)
        print(x)
    elif opcion == '7':
        break 