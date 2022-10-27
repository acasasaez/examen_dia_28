from Pila import Pila
def Torres_de_Hanoi (n, origen, destino, auxiliar):
    if n == 1:
        origen.apilar(1)
        origen.desapilar()
        destino.apilar(1)
        destino.mostrar()
    else:
        Torres_de_Hanoi (n-1, origen, auxiliar, destino)
        print ("Mover disco", n, "de la torre", origen, "a la torre", destino)
        
        destino.desapilar(1)
        destino.apilar(n)
        Torres_de_Hanoi (n-1, auxiliar, destino, origen)
A = Pila()
B = Pila()
C = Pila()
Torres_de_Hanoi (5, A, C, B)
