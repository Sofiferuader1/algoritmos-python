class Pila:

    def __init__(self):
        self.datos = []


def apilar(pila, dato):
    pila.datos.append(dato)


def desapilar(pila):
    return pila.datos.pop()


def pila_vacia(pila):
    return len(pila.datos) == 0