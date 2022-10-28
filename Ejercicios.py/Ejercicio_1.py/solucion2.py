from pila import Pila
A = Pila()
B = Pila()
C = Pila()

def pila_inicial(n, origen):
    origen.apilar(n)
    if n >1:
        pila_inicial(n-1, origen)
        

pila_inicial(3, A)
print(A.__str__())

def Torres_de_Hanoi(n, origen, destino, auxiliar):
    if n > 0:
        Torres_de_Hanoi(n-1,origen, auxiliar, destino)
        destino.apilar(origen.desapilar())
        print(A.__str__(), B.__str__(), C.__str__(), '##############', sep='\n')
        Torres_de_Hanoi(n-1, auxiliar, destino, origen)

# Initiate call from source A to target C with auxiliary B
Torres_de_Hanoi(3, A, C, B)