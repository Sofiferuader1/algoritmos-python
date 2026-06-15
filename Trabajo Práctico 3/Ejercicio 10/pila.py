class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)

    def desapilar(self):
        if not self.pila_vacia():
            return self.elementos.pop()
        return None

    def pila_vacia(self):
        return len(self.elementos) == 0

    def tamanio(self):
        return len(self.elementos)

    def mostrar(self):
        for elemento in reversed(self.elementos):
            print(elemento)