from interfaz import (
    mostrar_titulo,
    mostrar_instrucciones,
    solicitar_rango,
    preguntar_repetir,
    mostrar_estadisticas_generales,
)

from juego import jugar_partida
from datos import cargar_estadisticas


def main():
    mostrar_titulo()

    while True:
        minimo, maximo = solicitar_rango()

        mostrar_instrucciones(minimo, maximo)

        jugar_partida(minimo, maximo)

        estadisticas = cargar_estadisticas()

        mostrar_estadisticas_generales(estadisticas)

        if not preguntar_repetir():
            print("\nGracias por jugar. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()