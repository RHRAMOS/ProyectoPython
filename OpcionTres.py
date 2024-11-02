def opcion_3():
  import math
  while True:
    print("Funciones trigonométricas ")
    print("1. math.sin(x) ")
    print("2. math.cos(x) ")
    print("3. math.tan(x): ")
    print("4. math.asin(x) ")
    print("5. math.acos(x) ")
    print("6. math.atan(x): ")
    print("7. math.atan2(y, x): ")
    print("8. math.hypot(x, y): ")
    print("9.SALIR ")
    opcion = input("Selecciona la operación que deseas realizar: ")
    
    if opcion == '1':
        x = math.sin(20)
        print("Devuelve el seno de x (en radianes).", x)
    elif opcion == '2':
        x = math.cos(58)
        print("Devuelve el coseno de x (en radianes).", x)
    elif opcion == '3':
        x = math.tan(251)
        print(f"Devuelve la tangente de x (en radianes). {x}")
    elif opcion == '4':
        x = math.asin(0.5)
        print("Devuelve el arco seno de x (en radianes).",x)
    elif opcion == '5':
        x = math.acos(0.3)
        print(f"Devuelve el arco coseno de x (en radianes). {x}")
    elif opcion == '6':  
        x = math.atan(9)
        print(" Devuelve el arco tangente de x (en radianes).",x)
    elif opcion == '7':  
        x = math.atan2(2, 5)
        print("Devuelve el arco tangente de y/x teniendo en cuenta los signos de ambos argumentos para determinar el cuadrante correcto.",x)
    elif opcion == '8':
         x = math.hypot(2, 8)
         print(x)
    elif opcion == '9':     
        break