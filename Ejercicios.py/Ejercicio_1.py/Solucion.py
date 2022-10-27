#Solución sin Pilas, trabajo con funciones recursivas
def Torres_de_Hanoi (n, origen, destino, auxiliar): #Empezamos creando la función Torres_de_Hanoi que nos devolverá los movimientos que se deben hacer para solucionar
    #el juego de la manera  optima
    #n: número de discos de la torre
    #origen: torre de origen
    #destino: torre de destino (donde debe acabar la torre de Hanoi)
    #auxiliar: torre que nos permite llevar a cabo los movimientos para trasladar los discos de la torre de origen a la torre de destino
    
    if n == 1: # Empezamos analizando el caso base, que n = 1, entonces solo tendríamos que mover el disco del origen al destino
        # si n es 1
        print ("Mover disco 1 de", origen, "a", destino) #Entonces el disco 1 se traslada a la torre de destino y se acaba el juego
#Sin embargo, el problema se complica cuando el tamaño de n comienza a aumentar.
#Ahora debemos transladar los n discos a la torre de destino bajo las siguientes condiciones:
#1. No se puede colocar un disco sobre otro más pequeño
#2. Solo se puede mover un disco a la vez
#Contamos con la ventaja de que tenemos una torre auxiliar que nos permitirá realizar los movimientos
#La manera óptima de llegar al resultado es a través de 2**n - 1 movimientos
#para esto haremos dos llamadas recursivas de nuestra función Torres_de_Hanoi
    else: # en caso de que n no sea 1
        Torres_de_Hanoi (n-1, origen, auxiliar, destino) #Llamada recursiva 1
        print ("Mover disco", n, "de", origen, "a", destino)
            
        Torres_de_Hanoi (n-1, auxiliar, destino, origen) #Llamada recursiva 2
    print("El número de movimientos para resolver este juego es ")
    return 2**n - 1 
