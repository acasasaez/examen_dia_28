import csv
class Nave():
    def __init__(self, nombre,largo, tripulacion, cantidad_pasajeros ):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.cantidad_pasajeros = cantidad_pasajeros
    
class Naves ():
    lista =[]
    def guardar (n):
        with open("resultados.csv.csv", "w",newline = "") as file: 
            writer =csv.writer(file, delimiter = "," )
            writer.writerow( ["TABLA DE DATOS RESULTADOS"])
            writer.writerows(n)
    @staticmethod
    def crear(nombre, largo, tripulacion, cantidad_pasajeros):
            nave = Nave(nombre, largo, tripulacion, cantidad_pasajeros)
            Naves.lista.append(nave)
            Naves.guardar(nave)
            return nave
