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
        "mejor_intentos": None
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
            return json.load(archivo)

    except (json.JSONDecodeError, OSError):
        return estadisticas_iniciales()


def guardar_resultado(intentos, completada):
    estadisticas = cargar_estadisticas()

    estadisticas["partidas"] += 1

    if completada:
        estadisticas["completadas"] += 1

        mejor = estadisticas["mejor_intentos"]

        if mejor is None or intentos < mejor:
            estadisticas["mejor_intentos"] = intentos

    else:
        estadisticas["contradicciones"] += 1

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