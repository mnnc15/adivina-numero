def mostrar_titulo():
    print("=" * 46)
    print("          JUEGO ADIVINA EL NÚMERO")
    print("=" * 46)


def mostrar_instrucciones(minimo, maximo):
    print(f"\nPiensa un número entero entre {minimo} y {maximo}.")
    print("No me lo digas.")
    print("Yo intentaré adivinarlo.")
    print("Responde únicamente con: mayor, menor o correcto.")

    input("\nPresiona Enter cuando estés listo...")


def solicitar_entero(mensaje):
    while True:
        valor = input(mensaje).strip()

        try:
            return int(valor)
        except ValueError:
            print("Error: debes ingresar un número entero.")


def solicitar_rango():
    while True:
        print("\n--- CONFIGURACIÓN DEL RANGO ---")

        minimo = solicitar_entero("Valor mínimo: ")
        maximo = solicitar_entero("Valor máximo: ")

        if minimo < maximo:
            return minimo, maximo

        print("Error: el valor mínimo debe ser menor que el máximo.")


def solicitar_respuesta():
    while True:
        respuesta = input(
            "¿Tu número es mayor, menor o correcto?: "
        ).strip().lower()

        if respuesta in ("mayor", "menor", "correcto"):
            return respuesta

        print("Respuesta inválida. Usa: mayor, menor o correcto.")


def preguntar_repetir():
    while True:
        respuesta = input(
            "\n¿Deseas jugar nuevamente? (s/n): "
        ).strip().lower()

        if respuesta == "s":
            return True
        elif respuesta == "n":
            return False

        print("Respuesta inválida. Escribe s o n.")


def mostrar_estadisticas_generales(estadisticas):
    print("\n--- ESTADÍSTICAS GENERALES ---")
    print(f"Partidas registradas: {estadisticas['partidas']}")
    print(f"Partidas completadas: {estadisticas['completadas']}")
    print(f"Partidas con contradicción: {estadisticas['contradicciones']}")

    if estadisticas["mejor_intentos"] is not None:
        print(
            f"Mejor resultado: "
            f"{estadisticas['mejor_intentos']} intento(s)"
        )