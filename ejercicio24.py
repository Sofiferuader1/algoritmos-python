from pila import Pila, apilar, desapilar, pila_vacia

personajes = Pila()
auxiliar = Pila()

#apilo (persona, peliculas que hizo)

apilar(personajes, ("Iron Man", 10))
apilar(personajes, ("Groot", 6))
apilar(personajes, ("Rocket Raccoon", 5))
apilar(personajes, ("Black Widow", 8))
apilar(personajes, ("Thor", 9))


print("POSICIONES DE ROCKET RACCOON Y GROOT")

posicion = 1

while not pila_vacia(personajes):

    personaje = desapilar(personajes)

    nombre = personaje[0]
    peliculas = personaje[1]

    if nombre == "Rocket Raccoon":
        print("Rocket Raccoon está en la posición", posicion)

    if nombre == "Groot":
        print("Groot está en la posición", posicion)

    apilar(auxiliar, personaje)

    posicion += 1 # es una forma abreviada de escribir posicion = posicion + 1


print("\nPERSONAJES CON MÁS DE 5 PELÍCULAS")

while not pila_vacia(auxiliar):

    personaje = desapilar(auxiliar)

    nombre = personaje[0]
    peliculas = personaje[1]

    if peliculas > 5:
        print(nombre, "participó en", peliculas, "películas")

    apilar(personajes, personaje)

print("\nPELÍCULAS DE BLACK WIDOW")

while not pila_vacia(personajes):

    personaje = desapilar(personajes)

    nombre = personaje[0]
    peliculas = personaje[1]

    if nombre == "Black Widow":
        print("Black Widow participó en", peliculas, "películas")

    apilar(auxiliar, personaje)

print("\nPERSONAJES QUE EMPIEZAN CON C, D Y G") # /n es para que haga un salto de línea

while not pila_vacia(auxiliar):

    personaje = desapilar(auxiliar)

    nombre = personaje[0]

    if nombre.startswith("C") or nombre.startswith("D") or nombre.startswith("G"): # startswith sirve para verificar con qué letra empieza un texto
        print(nombre)

    apilar(personajes, personaje)

