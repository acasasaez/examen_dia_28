class Cola():
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def agregar(self, x):
        self.items.append(x)

    def avanzar(self):
        return self.items.pop(0)

    def longitud(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)