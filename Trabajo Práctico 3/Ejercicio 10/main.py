from cola import Cola
from pila import Pila


def eliminar_notificaciones_facebook(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        notificacion = cola.atencion()

        if notificacion["aplicacion"] != "Facebook":
            cola.arribo(notificacion)


def mostrar_twitter_python(cola):
    cantidad = cola.tamanio()

    for _ in range(cantidad):
        notificacion = cola.atencion()

        if (
            notificacion["aplicacion"] == "Twitter"
            and "Python" in notificacion["mensaje"]
        ):
            print(notificacion)

        cola.arribo(notificacion)


def guardar_notificaciones_entre_horas(cola):
    pila_temporal = Pila()
    cantidad = cola.tamanio()

    hora_inicio = "11:43"
    hora_fin = "15:57"

    for _ in range(cantidad):
        notificacion = cola.atencion()

        if hora_inicio <= notificacion["hora"] <= hora_fin:
            pila_temporal.apilar(notificacion)

        cola.arribo(notificacion)

    return pila_temporal


cola_notificaciones = Cola()

cola_notificaciones.arribo({
    "hora": "10:30",
    "aplicacion": "Facebook",
    "mensaje": "Nueva solicitud de amistad"
})

cola_notificaciones.arribo({
    "hora": "11:50",
    "aplicacion": "Twitter",
    "mensaje": "Nuevo hilo sobre Python"
})

cola_notificaciones.arribo({
    "hora": "12:20",
    "aplicacion": "Instagram",
    "mensaje": "Nuevo me gusta en tu foto"
})

cola_notificaciones.arribo({
    "hora": "14:15",
    "aplicacion": "Facebook",
    "mensaje": "Tienes un nuevo comentario"
})

cola_notificaciones.arribo({
    "hora": "15:30",
    "aplicacion": "Twitter",
    "mensaje": "Python es tendencia"
})

cola_notificaciones.arribo({
    "hora": "16:10",
    "aplicacion": "WhatsApp",
    "mensaje": "Mensaje nuevo"
})


print("COLA ORIGINAL:")
cola_notificaciones.mostrar()

print("\nNOTIFICACIONES DE TWITTER CON LA PALABRA PYTHON:")
mostrar_twitter_python(cola_notificaciones)

print("\nELIMINANDO NOTIFICACIONES DE FACEBOOK...")
eliminar_notificaciones_facebook(cola_notificaciones)

print("\nCOLA SIN NOTIFICACIONES DE FACEBOOK:")
cola_notificaciones.mostrar()

pila_temporal = guardar_notificaciones_entre_horas(cola_notificaciones)

print("\nNOTIFICACIONES ENTRE 11:43 Y 15:57:")
pila_temporal.mostrar()

print("\nCANTIDAD DE NOTIFICACIONES ENTRE 11:43 Y 15:57:")
print(pila_temporal.tamanio())