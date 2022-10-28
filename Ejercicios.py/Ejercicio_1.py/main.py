from solucion2 import *

def inicio():
    print("Elija el numero de discos para el juego de las torres de Hanoi")
    discos = int(input())
    pila_inicial(discos, A)
    Torres_de_Hanoi(discos, A, C, B)
    
    print("Felicidades, ha ganado el juego")
    print("Ha realizado", 2**discos -1, "movimientos")
    print("Desea volver a jugar?")
    print("1. Si")
    print("2. No")
    opcion = int(input())
    if opcion == 1:
        inicio()
    elif opcion == 2:
        print("Gracias por jugar")
