from interfaz import (
    solicitar_respuesta,
    preguntar_corregir_contradiccion
)
from datos import guardar_resultado


def calcular_intento(minimo, maximo):
    return (minimo + maximo) // 2


def calcular_puntaje(rango_minimo, rango_maximo, intentos):
    cantidad_numeros = rango_maximo - rango_minimo + 1

    puntaje_base = cantidad_numeros * 10
    penalizacion = intentos * 20

    puntaje = puntaje_base - penalizacion

    if puntaje < 0:
        puntaje = 0

    return puntaje


def jugar_partida(minimo, maximo):
    rango_minimo_inicial = minimo
    rango_maximo_inicial = maximo

    intentos = 0
    historial_intentos = []

    while minimo <= maximo:
        rango_anterior_minimo = minimo
        rango_anterior_maximo = maximo

        intento = calcular_intento(minimo, maximo)
        intentos += 1

        print(f"\nIntento #{intentos}")
        print(f"¿Tu número es {intento}?")

        respuesta = solicitar_respuesta()

        historial_intentos.append({
            "intento": intentos,
            "numero": intento,
            "respuesta": respuesta
        })

        if respuesta == "correcto":
            puntaje = calcular_puntaje(
                rango_minimo_inicial,
                rango_maximo_inicial,
                intentos
            )

            print(f"\n¡Lo adiviné! Tu número es {intento}.")
            print(f"Necesité {intentos} intento(s).")
            print(f"Puntaje obtenido: {puntaje} puntos.")

            guardar_resultado(
                intentos,
                True,
                rango_minimo_inicial,
                rango_maximo_inicial,
                intento,
                puntaje,
                historial_intentos
            )

            return

        if respuesta == "mayor":
            minimo = intento + 1

        elif respuesta == "menor":
            maximo = intento - 1

        if minimo > maximo:
            print("\nNo existe un número que coincida con tus respuestas.")
            print("Se detectó una posible contradicción.")

            corregir = preguntar_corregir_contradiccion()

            if corregir:
                minimo = rango_anterior_minimo
                maximo = rango_anterior_maximo

                intentos -= 1

                historial_intentos.pop()

                print("\nÚltima respuesta eliminada.")
                print("Volvamos a intentarlo...")

                continue

            guardar_resultado(
                intentos,
                False,
                rango_minimo_inicial,
                rango_maximo_inicial,
                None,
                0,
                historial_intentos
            )

            return

        print(f"Rango restante: {minimo} a {maximo}")