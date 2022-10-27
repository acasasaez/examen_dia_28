from Pila import Pila
def Torres_de_Hanoi (n, origen, destino, auxiliar):
    if n == 1:
        a = n
        origen.apilar(a)
        origen.desapilar()
        destino.apilar(a)
        print ("Mover disco 1 de ",origen,"a",destino)

    Torres_de_Hanoi (n-1, origen, auxiliar, destino)
    
    print ("Mover disco", n, "de la torre", origen, "a la torre", destino)
    Torres_de_Hanoi (n-1, auxiliar, destino, origen)
A = Pila()
B = Pila()
C = Pila()
Torres_de_Hanoi (5, A, C, B)
