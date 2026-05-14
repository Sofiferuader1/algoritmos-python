from pila import Pila, apilar, desapilar, pila_vacia

movimientos = Pila()

cantidad_movimientos = int(input("¿Cuántos cambios de dirección realizó el robot?: "))

for i in range(cantidad_movimientos):
    print("Movimiento", i + 1)

    pasos = int(input("Ingrese cantidad de pasos: "))
    direccion = input("Ingrese dirección: ")

    while direccion not in ["norte", "sur", "este", "oeste",
                            "noreste", "noroeste",
                            "sureste", "suroeste"]:

        print("Dirección inválida")
        direccion = input("Ingrese una dirección válida: ")

    apilar(movimientos, (pasos, direccion))


print("\nCAMINO DE REGRESO")

while not pila_vacia(movimientos):

    pasos, direccion = desapilar(movimientos)

    if direccion == "norte":
        vuelta = "sur"
    elif direccion == "sur":
        vuelta = "norte"
    elif direccion == "este":
        vuelta = "oeste"
    elif direccion == "oeste":
        vuelta = "este"
    elif direccion == "noreste":
        vuelta = "suroeste"
    elif direccion == "noroeste":
        vuelta = "sureste"
    elif direccion == "sureste":
        vuelta = "noroeste"
    elif direccion == "suroeste":
        vuelta = "noreste"

    print("Mover", pasos, "pasos hacia", vuelta)