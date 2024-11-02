import math
def opcion_2():
  while True:
    print ("Funciones matematicas del módulo math")
    print("1. math.sqrt(x): ")
    print("2. math.exp(x): ")
    print("3. math.log(x, base: ")
    print("4. math.log10(x): ")
    print("5. math.log2(x): ")
    print("6. math.factorial(x): ")
    print("7. math.gcd(a, b): ")
    print("8. math.isqrt(x): ")
    print("9. math.copysign(x, y) ")
    print("10. math.fabs(x): ")
    print("11. math.ceil(x): ")
    print("12. math.floor(x) ")
    print("13. math.trunc(x) ")
    print("14. math.fmod(x, y): ")
    print("15. math.remainder(x, y):")
    print("16. math.prod(iterable): ")
    print("17. ATRAS ")
    opcion = input("Selecciona la operación que deseas realizar: ")
  
    if opcion == '1':
        x = math.sqrt(15)
        print("Devuelve la raíz cuadrada de x.",x)
    elif opcion == '2':
        x = math.exp(35)
        print("Devuelve el valor de e elevado a la potencia x (e^x)",x)
    elif opcion == '3':
        x = math.log(40,2)
        print("Devuelve el logaritmo de x en la base especificada. Si no se especifica la base, calcula el logaritmo natural (base = e).",x)
    elif opcion == '4':
        x = math.log10(52.9)
        print(" Devuelve el logaritmo base 10 de x.", x)
    elif opcion == '5':  
    
        x = math.log2(25)
        print(x)
    elif opcion == '6':
        x = math.factorial(33)
        print("Devuelve el factorial de un número entero x.", x)
    elif opcion == '7':
        x = math.gcd(8, 6)
        print(f"Devuelve el máximo común divisor de a y b. {x}")
    elif opcion == '8':
        x = math.isqrt(69)
        print("Devuelve la raíz cuadrada entera de x.", x)
    elif opcion == '9':
        x = math.copysign(20, 17)
        print("Devuelve x con el signo de y.", x)
    elif opcion == '10':
        x = math.fabs(15)
        print("Devuelve el valor absoluto de x como flotante.", x)
    elif opcion == '11':
        x = math.ceil(789.5)
        print("Devuelve el menor entero mayor o igual a x.", x)
    elif opcion == '12':
        x = math.floor(468.78)
        print("Devuelve el mayor entero menor o igual a x.", x)
    elif opcion == '13':
        x = math.trunc(458.9)
        print("Elimina la parte decimal de x, devolviendo solo la parte entera.",x)
    elif opcion == '14':
        x = math.fmod(15, 7)
        print(x)
    elif opcion == '15':
        x = math.remainder(8, 3)
        print(x)
    elif opcion == '16':
        iterable = (15, 28)
        x = math.prod(iterable)
        print(x) 
    elif opcion == '17':
        break 