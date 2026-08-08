from interfaz import solicitar_respuesta
from datos import guardar_resultado


def calcular_intento(minimo, maximo):
    # Usa el punto medio para reducir el rango de búsqueda.
    return (minimo + maximo) // 2


def jugar_partida(minimo, maximo):
    intentos = 0

    while minimo <= maximo:
        intento = calcular_intento(minimo, maximo)
        intentos += 1

        print(f"\nIntento #{intentos}")
        print(f"¿Tu número es {intento}?")

        respuesta = solicitar_respuesta()

        if respuesta == "correcto":
            print(f"\n¡Lo adiviné! Tu número es {intento}.")
            print(f"Necesité {intentos} intento(s).")

            guardar_resultado(intentos, True)
            return

        if respuesta == "mayor":
            minimo = intento + 1

        elif respuesta == "menor":
            maximo = intento - 1

        # Un rango vacío indica respuestas contradictorias.
        if minimo > maximo:
            print("\nNo existe un número que coincida con tus respuestas.")
            print("Se detectó una posible contradicción.")

            guardar_resultado(intentos, False)
            return

        print(f"Rango restante: {minimo} a {maximo}")