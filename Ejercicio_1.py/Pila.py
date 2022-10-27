class Pila():
    def __init__(self):
        self.items = []
    
    def mostrar (self):
        print (self.items)

    def estaVacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def longitud(self):
        return len(self.items)
