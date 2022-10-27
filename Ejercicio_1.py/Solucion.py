from Pila import Pila
def Torres_de_Hanoi (n, origen, destino, auxiliar):
    
    if n == 1:
        
        destino.apilar(origen.desapilar())

    else:
        Torres_de_Hanoi(n-1, origen, auxiliar, destino)
        Torres_de_Hanoi(1, origen, destino, auxiliar)
        Torres_de_Hanoi(n-1, auxiliar, destino, origen)

    return destino.mostrar()

origen = Pila()
destino = Pila()
auxiliar = Pila()
n = int(input("Ingrese la cantidad de discos: "))
print("Torres de Hanoi con", n, "discos")
print (Torres_de_Hanoi(n, origen, destino, auxiliar))
