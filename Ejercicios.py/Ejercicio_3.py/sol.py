
class Nave():
    def __init__(self, nombre,largo, cantidad_tripulacion, cantidad_pasajeros ):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = cantidad_tripulacion
        self.cantidad_pasajeros = cantidad_pasajeros
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Largo: ",self.largo)
        print("Tripulacion: ",self.tripulacion)
        print("Cantidad de pasajeros: ",self.cantidad_pasajeros)


