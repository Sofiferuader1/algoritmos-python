from collections import deque


class Cola:
    def __init__(self):
        self.elementos = deque()

    def arribo(self, dato):
        self.elementos.append(dato)

    def atencion(self):
        if not self.cola_vacia():
            return self.elementos.popleft()
        return None

    def cola_vacia(self):
        return len(self.elementos) == 0

    def tamanio(self):
        return len(self.elementos)

    def mostrar(self):
        for elemento in self.elementos:
            print(elemento)