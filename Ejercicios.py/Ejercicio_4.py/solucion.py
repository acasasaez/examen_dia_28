class Polinomio():
    def __init__(self, coeficientes, grado):
        self.coeficientes = coeficientes
        self.grado = grado

    def __str__(self):
        return f'Coeficientes: {self.coeficientes}, Grado: {self.grado}'
    
    def __suma__(self, otro):
        if self.grado == otro.grado:
            coeficientes = []
            for i in range(self.grado + 1):
                coeficientes.append(self.coeficientes[i] + otro.coeficientes[i])
            return Polinomio(coeficientes, self.grado)
        else:
            return "No se pueden sumar polinomios de distinto grado"

    def __resta__(self, otro):
        if self.grado == otro.grado:
            coeficientes = []
            for i in range(self.grado + 1):
                coeficientes.append(self.coeficientes[i] - otro.coeficientes[i])
            return Polinomio(coeficientes, self.grado)
        else:
            return "No se pueden restar polinomios de distinto grado"

    def __multiplicacion__(self, otro):
        coeficientes = []
        for i in range(self.grado + 1):
            coeficientes.append(self.coeficientes[i] * otro.coeficientes[i])
        return Polinomio(coeficientes, self.grado)
    
    def mostrar(self):
        for i in range(self.grado + 1):
            a= f'({self.coeficientes[i]})x^{self.grado - i} '
            if i != self.grado:
                a += '+ '
            print(a, end='')
        print()

