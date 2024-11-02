import math
def opcion_1():
  while True:
    print(" Funciones matemáticas incorporadas") 
    print("1. abs(x): ")
    print("2. round(x, n): ")
    print("3. pow(x, y): ")
    print("4. divmod(x, y): ")
    print("5. sum(iterable): ")
    print("6. min(iterable): ")
    print("7. max(iterable): . ")
    print("8. ATRÁS")
    opcion = input("Selecciona la operación que deseas realizar: ")
    
    if opcion == '1':
       x = abs(-7.25)
       print("Devuelve el valor absoluto de un número",x)
    elif opcion == '2':
        x = round(107.5)
        print("Redondea un número a n decimales .", x)
        x = round(66.69,2)
        print("o a un entero si no se especifica n)", x)
    elif opcion == '3':
        x = pow(4, 3)
        print(f"Calcula el valor de x elevado a la potencia y equivalente a x y {x}")
    elif opcion == '4':
        x = divmod(5, 2)
        print("Devuelve una tupla con el cociente y el resto de la división de x entre y.", x)
    elif opcion == '5':
        iterable = (1,2,8)
        x = sum(iterable)
        print("Suma los elementos de un iterable.", x)
    elif opcion == '6':
        iterable = (100,38,71)
        x = min(iterable)
        print("Devuelve el valor mínimo de un iterable",x)
    elif opcion == '7':
        iterable = (0,200,458)
        x = max(iterable)
        print("Devuelve el valor máximo de un iterable",x)
    elif opcion == '8':
        break 
  