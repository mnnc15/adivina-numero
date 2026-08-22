import json
from pathlib import Path


RUTA_DATOS = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "estadisticas.json"
)


def estadisticas_iniciales():
    return {
        "partidas": 0,
        "completadas": 0,
        "contradicciones": 0,
        "mejor_intentos": None,
        "mejor_puntaje": 0,
        "total_intentos": 0,
        "historial": []
    }


def cargar_estadisticas():
    if not RUTA_DATOS.exists():
        return estadisticas_iniciales()

    try:
        with open(
            RUTA_DATOS,
            "r",
            encoding="utf-8"
        ) as archivo:
            estadisticas = json.load(archivo)

        # Agrega campos nuevos si el archivo pertenece
        # a una versión anterior del programa.
        valores_iniciales = estadisticas_iniciales()

        for clave, valor in valores_iniciales.items():
            if clave not in estadisticas:
                estadisticas[clave] = valor

        return estadisticas

    except (json.JSONDecodeError, OSError):
        return estadisticas_iniciales()


def guardar_estadisticas(estadisticas):
    RUTA_DATOS.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(
        RUTA_DATOS,
        "w",
        encoding="utf-8"
    ) as archivo:
        json.dump(
            estadisticas,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def guardar_resultado(
    intentos,
    completada,
    rango_minimo,
    rango_maximo,
    numero_adivinado=None,
    puntaje=0,
    historial_intentos=None
):
    estadisticas = cargar_estadisticas()

    estadisticas["partidas"] += 1
    estadisticas["total_intentos"] += intentos

    if completada:
        estadisticas["completadas"] += 1

        mejor = estadisticas["mejor_intentos"]

        if mejor is None or intentos < mejor:
            estadisticas["mejor_intentos"] = intentos

        if puntaje > estadisticas["mejor_puntaje"]:
            estadisticas["mejor_puntaje"] = puntaje

        resultado = "completada"

    else:
        estadisticas["contradicciones"] += 1
        resultado = "contradiccion"

    partida = {
        "rango_minimo": rango_minimo,
        "rango_maximo": rango_maximo,
        "numero_adivinado": numero_adivinado,
        "intentos": intentos,
        "puntaje": puntaje,
        "resultado": resultado,
        "detalle_intentos": historial_intentos or []
    }

    estadisticas["historial"].append(partida)

    guardar_estadisticas(estadisticas)