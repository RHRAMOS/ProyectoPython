import math
import OpcionUno
import OpcionDos
import OpcionTres
import OpcionCuatro
import OpcionCinco
import OpcionSeis
print("Richard Ramos")
print ("BOSA SABADOS ")
def mostar_menu():
 print("1. Funciones matemáticas incorporadas")
 print("2. Funciones matematicas del módulo math")
 print("3. Funciones trigonométricas")
 print("4. Funciones hiperbólicas")
 print("5. Funciones de constantes")
 print("6. Otras funciones avanzadas")
 print("7. SALIR ")


while True:
    mostar_menu()
     
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == '1':
      OpcionUno.opcion_1()
      
    elif opcion == '2':
        OpcionDos.opcion_2()
        
    elif opcion =='3':
        OpcionTres.opcion_3()
        
    elif opcion =='4':
        OpcionCuatro.opcion_4()
        
    elif opcion =='5':
        OpcionCinco.opcion_5()
    
    elif opcion =='6':
        OpcionSeis.opcion_6()
        
    elif opcion =='7':
        print("Fue un gusto ayudarte. Hasta Pronto")
        break









