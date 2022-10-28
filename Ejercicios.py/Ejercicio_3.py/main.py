from sol import *
from cola import *
Maria = Nave("Maria", 18, 20,2)
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

def nave_mas_tripulacion():
    for i in Naves.__str__():
        if i.tripulacion == max(Naves.items, key=lambda x: x.tripulacion).tripulacion:
            i.mostrar()

nave_mas_pasajeros()
nave_mas_tripulacion()

def nave_mas_largo():
    for i in Naves_2.__str__():
        if i.largo == max(Naves_2.items, key=lambda x: x.largo).largo:
            i.mostrar()

def nave_mas_corta():
    for i in Naves_2.__str__():
        if i.largo == min(Naves_2.items, key=lambda x: x.largo).largo:
            i.mostrar()

nave_mas_largo()
nave_mas_corta()

Naves_3 = Cola()
def naves_6_pasajeros():
    for i in Naves.__str__():
        if i.cantidad_pasajeros >= 6:
            Naves_3.agregar(i)
    return Naves_3.__str__()

naves_6_pasajeros()

for i in Naves_3.__str__():
        i.mostrar()
        print(" ")

Naves_4 = Cola()
def naves_inician_At():
    for i in Naves.__str__():
        if i.nombre[0] == "A" and i.nombre[1] == "t":
            Naves_4.agregar(i)
    return Naves_4.__str__()

naves_inician_At()
for i in Naves_4.__str__():
        i.mostrar()

def inicio():
    print("1.Ver naves ordenadas alfabeticamente")
    print("2. Ver naves ordenadas por largo")
    print("3. Nave con mas pasajeros")
    print("4. Nave con mas tripulacion")
    print("5. Nave mas larga")
    print("6. Nave mas corta")
    print("7. Naves con mas de 6 pasajeros")
    print("8. Naves que inician con Atun")
    print("9. Salir")
    opcion = int(input("Que desea hacer? "))
    if opcion == 1:
        añadir_naves_orden_alfabetico()
        for i in Naves.__str__():
           i.mostrar()
           print(" ")
        inicio()
    elif opcion == 2:
        añadir_naves_orden_largo()
        for i in Naves_2.__str__():
           i.mostrar()
           print(" ")
        inicio()

    elif opcion == 3:
        nave_mas_pasajeros()

        inicio()
    elif opcion == 4:
        nave_mas_tripulacion()
        inicio()
    elif opcion == 5:
        nave_mas_largo()
        inicio()
    elif opcion == 6:
        nave_mas_corta()
        inicio()
    elif opcion == 7:
        naves_6_pasajeros()
        for i in Naves_3.__str__():
            i.mostrar()
            print(" ")
        inicio()
    elif opcion == 8:
        naves_inician_At()
        inicio()
    elif opcion == 9:
        print("Hasta luego")
    else:
        print("Opcion incorrecta")
        inicio()