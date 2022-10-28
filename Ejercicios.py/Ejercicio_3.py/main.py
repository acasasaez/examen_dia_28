from sol import *
from cola import *
Maria = Nave("Maria", 18, 20,100)
Atun = Nave("Atun", 15, 10, 50)
Halcon_Milenario = Nave("Halcon_Milenario", 100, 100, 1000)
Estrella_de_la_muerte = Nave("Estrella_de_la_muerte", 1000, 1000, 10000)
Manolo= Nave("Manolo", 10, 10, 10)
Pedro= Nave("Pedro", 10, 3, 10)
Naves = Cola()

Halcon_Milenario.mostrar()
Estrella_de_la_muerte.mostrar()

def añadir_naves_orden_alfabetico():
    Naves.agregar(Maria)
    Naves.agregar(Atun)
    Naves.agregar(Halcon_Milenario)
    Naves.agregar(Estrella_de_la_muerte)
    Naves.agregar(Manolo)
    Naves.agregar(Pedro)
    Naves.items.sort(key=lambda x: x.nombre)
    return Naves.__str__()
#for i in Naves.__str__():
        #i.mostrar()
        #print(" ")
añadir_naves_orden_alfabetico()

Naves_2 = Cola()
def añadir_naves_orden_largo():
    Naves_2.agregar(Maria)
    Naves_2.agregar(Atun)
    Naves_2.agregar(Halcon_Milenario)
    Naves_2.agregar(Estrella_de_la_muerte)
    Naves_2.agregar(Manolo)
    Naves_2.agregar(Pedro)
    Naves_2.items.sort(key=lambda x: x.largo)
    return Naves_2.__str__()
#for i in Naves_2.__str__():
        #i.mostrar()
        #print(" ")
añadir_naves_orden_largo()

def nave_mas_pasajeros():
    for i in Naves.__str__():
        if i.cantidad_pasajeros == max(Naves.items, key=lambda x: x.cantidad_pasajeros).cantidad_pasajeros:
            i.mostrar()



