import tkinter as tk
from tkinter import messagebox
import math


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


def seleccionar_modo():
    while True:
        print("\n--- MODO DE JUEGO ---")
        print("1. Clásico       (1 - 100)")
        print("2. Experto       (1 - 1000)")
        print("3. Personalizado")

        opcion = input("Selecciona un modo: ").strip()

        if opcion == "1":
            return 1, 100

        elif opcion == "2":
            return 1, 1000

        elif opcion == "3":
            return solicitar_rango()

        print("Opción inválida. Escribe 1, 2 o 3.")


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


def preguntar_corregir_contradiccion():
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Corregir mi última respuesta")
        print("2. Terminar la partida")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            return True

        elif opcion == "2":
            return False

        print("Opción inválida. Escribe 1 o 2.")


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


def mostrar_como_jugar():
    messagebox.showinfo(
        "Cómo jugar",
        "1. Selecciona un modo de juego.\n"
        "2. Piensa un número dentro del rango indicado.\n"
        "3. El computador intentará adivinarlo.\n"
        "4. Responde si tu número es mayor, menor o correcto.\n"
        "5. Intenta mantener respuestas coherentes."
    )

def abrir_pantalla_victoria(
    ventana_principal,
    ventana_partida,
    numero,
    intentos,
    puntaje,
    minimo,
    maximo
):
    ventana_partida.withdraw()

    ventana_victoria = tk.Toplevel(
        ventana_principal
    )

    ventana_victoria.title(
        "¡Número encontrado!"
    )

    ventana_victoria.geometry(
        "600x650"
    )

    ventana_victoria.resizable(
        False,
        False
    )

    ventana_victoria.configure(
        bg="#111827"
    )

    cantidad_numeros = (
        maximo
        - minimo
        + 1
    )

    maximo_esperado = max(
        1,
        math.ceil(
            math.log2(
                cantidad_numeros + 1
            )
        )
    )

    proporcion = (
        intentos
        / maximo_esperado
    )

    if proporcion <= 0.4:
        estrellas = "★★★★★"
        valoracion = "EXCELENTE"

    elif proporcion <= 0.6:
        estrellas = "★★★★☆"
        valoracion = "MUY BIEN"

    elif proporcion <= 0.8:
        estrellas = "★★★☆☆"
        valoracion = "BUEN RESULTADO"

    elif proporcion <= 1:
        estrellas = "★★★☆☆"
        valoracion = "COMPLETADO EFICIENTEMENTE"

    else:
        estrellas = "★★☆☆☆"
        valoracion = "RESULTADO MEJORABLE"

    titulo = tk.Label(
        ventana_victoria,
        text="¡TE ENCONTRÉ!",
        font=("Arial", 28, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(45, 10)
    )

    subtitulo = tk.Label(
        ventana_victoria,
        text="El número que estabas pensando era:",
        font=("Arial", 13),
        bg="#111827",
        fg="#94a3b8"
    )
    subtitulo.pack(
        pady=(0, 15)
    )

    etiqueta_numero = tk.Label(
        ventana_victoria,
        text=str(numero),
        font=("Arial", 58, "bold"),
        bg="#111827",
        fg="#facc15"
    )
    etiqueta_numero.pack(
        pady=10
    )

    marco_resultado = tk.Frame(
        ventana_victoria,
        bg="#1e293b",
        padx=40,
        pady=25
    )
    marco_resultado.pack(
        padx=70,
        pady=20,
        fill="x"
    )

    tk.Label(
        marco_resultado,
        text=f"Intentos realizados: {intentos}",
        font=("Arial", 13),
        bg="#1e293b",
        fg="white"
    ).pack(
        pady=5
    )

    tk.Label(
        marco_resultado,
        text=f"Puntaje obtenido: {puntaje}",
        font=("Arial", 13, "bold"),
        bg="#1e293b",
        fg="white"
    ).pack(
        pady=5
    )

    tk.Label(
        marco_resultado,
        text=f"Máximo esperado: {maximo_esperado} intentos",
        font=("Arial", 11),
        bg="#1e293b",
        fg="#94a3b8"
    ).pack(
        pady=5
    )

    etiqueta_estrellas = tk.Label(
        ventana_victoria,
        text=estrellas,
        font=("Arial", 25, "bold"),
        bg="#111827",
        fg="#facc15"
    )
    etiqueta_estrellas.pack(
        pady=(10, 5)
    )

    etiqueta_valoracion = tk.Label(
        ventana_victoria,
        text=valoracion,
        font=("Arial", 15, "bold"),
        bg="#111827",
        fg="white"
    )
    etiqueta_valoracion.pack(
        pady=(0, 25)
    )

    def jugar_nuevamente():
        ventana_victoria.destroy()
        ventana_partida.destroy()

        abrir_seleccion_modo(
            ventana_principal
        )

    def volver_menu():
        ventana_victoria.destroy()
        ventana_partida.destroy()

    marco_botones = tk.Frame(
        ventana_victoria,
        bg="#111827"
    )
    marco_botones.pack(
        pady=15
    )

    boton_jugar = tk.Button(
        marco_botones,
        text="JUGAR DE NUEVO",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=jugar_nuevamente
    )
    boton_jugar.grid(
        row=0,
        column=0,
        padx=10
    )

    boton_menu = tk.Button(
        marco_botones,
        text="MENÚ PRINCIPAL",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=volver_menu
    )
    boton_menu.grid(
        row=0,
        column=1,
        padx=10
    )

    ventana_victoria.protocol(
        "WM_DELETE_WINDOW",
        volver_menu
    )

def abrir_partida_grafica(
    ventana_principal,
    minimo,
    maximo,
    nombre_modo
):
    from juego import calcular_intento, calcular_puntaje
    from datos import guardar_resultado

    ventana_partida = tk.Toplevel(ventana_principal)

    ventana_partida.title("Partida - Adivina el Número")
    ventana_partida.geometry("1000x780")
    ventana_partida.resizable(False, False)
    ventana_partida.configure(bg="#111827")

    estado = {
        "minimo_inicial": minimo,
        "maximo_inicial": maximo,
        "minimo": minimo,
        "maximo": maximo,
        "intentos": 0,
        "intento_actual": None,
        "historial": []
    }

    titulo = tk.Label(
        ventana_partida,
        text="ADIVINA EL NÚMERO",
        font=("Arial", 24, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(pady=(35, 5))

    etiqueta_modo = tk.Label(
        ventana_partida,
        text=f"Modo: {nombre_modo}",
        font=("Arial", 12),
        bg="#111827",
        fg="#94a3b8"
    )
    etiqueta_modo.pack()

    instruccion = tk.Label(
        ventana_partida,
        text="Piensa en un número y responde:",
        font=("Arial", 14),
        bg="#111827",
        fg="white"
    )
    instruccion.pack(pady=(30, 10))

    etiqueta_intento = tk.Label(
        ventana_partida,
        text="Intento #1",
        font=("Arial", 15, "bold"),
        bg="#111827",
        fg="#cbd5e1"
    )
    etiqueta_intento.pack(pady=5)

    etiqueta_numero = tk.Label(
        ventana_partida,
        text="0",
        font=("Arial", 52, "bold"),
        bg="#111827",
        fg="white"
    )
    etiqueta_numero.pack(pady=15)

    pregunta = tk.Label(
        ventana_partida,
        text="¿Tu número es mayor, menor o correcto?",
        font=("Arial", 14),
        bg="#111827",
        fg="white"
    )
    pregunta.pack(pady=10)

    etiqueta_rango = tk.Label(
        ventana_partida,
        text="",
        font=("Arial", 12),
        bg="#111827",
        fg="#94a3b8"
    )
    etiqueta_rango.pack(pady=(25, 5))

    etiqueta_posibilidades = tk.Label(
        ventana_partida,
        text="",
        font=("Arial", 11),
        bg="#111827",
        fg="#94a3b8"
    )
    etiqueta_posibilidades.pack()

    canvas_rango = tk.Canvas(
        ventana_partida,
        width=540,
        height=90,
        bg="#111827",
        highlightthickness=0
    )
    canvas_rango.pack(pady=(15, 5))

    etiqueta_progreso = tk.Label(
        ventana_partida,
        text="",
        font=("Arial", 11, "bold"),
        bg="#111827",
        fg="#cbd5e1"
    )
    etiqueta_progreso.pack()

    marco_historial = tk.Frame(
        ventana_partida,
        bg="#1e293b",
        width=210,
        height=430
    )
    marco_historial.place(
        x=770,
        y=150
    )

    titulo_historial = tk.Label(
        marco_historial,
        text="HISTORIAL",
        font=("Arial", 14, "bold"),
        bg="#1e293b",
        fg="white"
    )
    titulo_historial.pack(
        pady=(15, 10)
    )

    lista_historial = tk.Listbox(
        marco_historial,
        width=27,
        height=20,
        font=("Arial", 10),
        bg="#0f172a",
        fg="white",
        selectbackground="#334155",
        borderwidth=0,
        highlightthickness=0
    )
    lista_historial.pack(
        padx=12,
        pady=5
    )

    def actualizar_historial_visual():
        lista_historial.delete(
            0,
            tk.END
        )

        if not estado["historial"]:
            lista_historial.insert(
                tk.END,
                "Sin intentos todavía"
            )
            return

        for registro in estado["historial"]:
            respuesta = registro["respuesta"]

            if respuesta == "mayor":
                texto_respuesta = "↑ Mayor"

            elif respuesta == "menor":
                texto_respuesta = "↓ Menor"

            else:
                texto_respuesta = "✓ Correcto"

            texto = (
                f"#{registro['intento']}   "
                f"{registro['numero']}   "
                f"{texto_respuesta}"
            )

            lista_historial.insert(
                tk.END,
                texto
            )

        lista_historial.see(
            tk.END
        )

    def actualizar_visual_rango():
        canvas_rango.delete("all")

        minimo_inicial = estado["minimo_inicial"]
        maximo_inicial = estado["maximo_inicial"]

        minimo_actual = estado["minimo"]
        maximo_actual = estado["maximo"]

        ancho_inicio = 40
        ancho_fin = 500
        y = 40

        diferencia_total = maximo_inicial - minimo_inicial

        def convertir_posicion(valor):
            proporcion = (
                (valor - minimo_inicial)
                / diferencia_total
            )

            return (
                ancho_inicio
                + proporcion
                * (ancho_fin - ancho_inicio)
            )

        x_minimo = convertir_posicion(minimo_actual)
        x_maximo = convertir_posicion(maximo_actual)

        canvas_rango.create_line(
            ancho_inicio,
            y,
            ancho_fin,
            y,
            fill="#475569",
            width=6
        )

        canvas_rango.create_line(
            x_minimo,
            y,
            x_maximo,
            y,
            fill="#22c55e",
            width=10
        )

        canvas_rango.create_text(
            ancho_inicio,
            68,
            text=str(minimo_inicial),
            fill="white"
        )

        canvas_rango.create_text(
            ancho_fin,
            68,
            text=str(maximo_inicial),
            fill="white"
        )

        if estado["intento_actual"] is not None:
            x_intento = convertir_posicion(
                estado["intento_actual"]
            )

            canvas_rango.create_oval(
                x_intento - 7,
                y - 7,
                x_intento + 7,
                y + 7,
                fill="#facc15",
                outline=""
            )

            canvas_rango.create_text(
                x_intento,
                15,
                text=str(estado["intento_actual"]),
                fill="#facc15",
                font=("Arial", 10, "bold")
            )

        posibilidades_iniciales = (
            maximo_inicial
            - minimo_inicial
            + 1
        )

        posibilidades_actuales = (
            maximo_actual
            - minimo_actual
            + 1
        )

        progreso = (
            1
            - posibilidades_actuales
            / posibilidades_iniciales
        ) * 100

        progreso = max(
            0,
            min(100, progreso)
        )

        etiqueta_progreso.config(
            text=(
                f"Progreso de búsqueda: "
                f"{progreso:.1f}%"
            )
        )

    def actualizar_informacion():
        etiqueta_rango.config(
            text=(
                f"Rango actual: "
                f"{estado['minimo']} - {estado['maximo']}"
            )
        )

        posibilidades = (
            estado["maximo"]
            - estado["minimo"]
            + 1
        )

        etiqueta_posibilidades.config(
            text=(
                f"Posibilidades restantes: "
                f"{posibilidades}"
            )
        )

        actualizar_visual_rango()

    def generar_intento():
        intento = calcular_intento(
            estado["minimo"],
            estado["maximo"]
        )

        estado["intento_actual"] = intento
        estado["intentos"] += 1

        etiqueta_intento.config(
            text=f"Intento #{estado['intentos']}"
        )

        etiqueta_numero.config(
            text=str(intento)
        )

        actualizar_informacion()

    def procesar_respuesta(respuesta):
        intento = estado["intento_actual"]

        minimo_anterior = estado["minimo"]
        maximo_anterior = estado["maximo"]

        estado["historial"].append({
            "intento": estado["intentos"],
            "numero": intento,
            "respuesta": respuesta
        })

        actualizar_historial_visual()

        if respuesta == "correcto":
            puntaje = calcular_puntaje(
                estado["minimo_inicial"],
                estado["maximo_inicial"],
                estado["intentos"]
            )

            guardar_resultado(
                estado["intentos"],
                True,
                estado["minimo_inicial"],
                estado["maximo_inicial"],
                intento,
                puntaje,
                estado["historial"]
            )

            abrir_pantalla_victoria(
                ventana_principal,
                ventana_partida,
                intento,
                estado["intentos"],
                puntaje,
                estado["minimo_inicial"],
                estado["maximo_inicial"]
            )

            return

        if respuesta == "mayor":
            estado["minimo"] = intento + 1

        elif respuesta == "menor":
            estado["maximo"] = intento - 1

        if estado["minimo"] > estado["maximo"]:
            corregir = messagebox.askyesno(
                "Contradicción detectada",
                "Tus respuestas produjeron una contradicción.\n\n"
                "¿Deseas corregir tu última respuesta?",
                parent=ventana_partida
            )

            if corregir:
                estado["minimo"] = minimo_anterior
                estado["maximo"] = maximo_anterior

                estado["intentos"] -= 1
                estado["historial"].pop()

                actualizar_historial_visual()

                generar_intento()
                return

            guardar_resultado(
                estado["intentos"],
                False,
                estado["minimo_inicial"],
                estado["maximo_inicial"],
                None,
                0,
                estado["historial"]
            )

            messagebox.showinfo(
                "Partida terminada",
                "La partida terminó por contradicción.",
                parent=ventana_partida
            )

            ventana_partida.destroy()
            return

        generar_intento()

    marco_botones = tk.Frame(
        ventana_partida,
        bg="#111827"
    )
    marco_botones.pack(pady=30)

    boton_menor = tk.Button(
        marco_botones,
        text="ES MENOR",
        font=("Arial", 12, "bold"),
        width=14,
        height=2,
        command=lambda: procesar_respuesta("menor")
    )
    boton_menor.grid(
        row=0,
        column=0,
        padx=8
    )

    boton_correcto = tk.Button(
        marco_botones,
        text="CORRECTO",
        font=("Arial", 12, "bold"),
        width=14,
        height=2,
        command=lambda: procesar_respuesta("correcto")
    )
    boton_correcto.grid(
        row=0,
        column=1,
        padx=8
    )

    boton_mayor = tk.Button(
        marco_botones,
        text="ES MAYOR",
        font=("Arial", 12, "bold"),
        width=14,
        height=2,
        command=lambda: procesar_respuesta("mayor")
    )
    boton_mayor.grid(
        row=0,
        column=2,
        padx=8
    )

    actualizar_historial_visual()
    generar_intento()


def seleccionar_modo_grafico(
    ventana_modo,
    minimo,
    maximo,
    nombre_modo
):
    ventana_principal = ventana_modo.master

    ventana_modo.destroy()

    abrir_partida_grafica(
        ventana_principal,
        minimo,
        maximo,
        nombre_modo
    )


def abrir_rango_personalizado(
    ventana_modo
):
    ventana_rango = tk.Toplevel(
        ventana_modo
    )

    ventana_rango.title(
        "Rango personalizado"
    )

    ventana_rango.geometry(
        "420x400"
    )

    ventana_rango.resizable(
        False,
        False
    )

    ventana_rango.configure(
        bg="#111827"
    )

    titulo = tk.Label(
        ventana_rango,
        text="RANGO PERSONALIZADO",
        font=("Arial", 19, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(40, 30)
    )

    etiqueta_minimo = tk.Label(
        ventana_rango,
        text="Valor mínimo:",
        font=("Arial", 12),
        bg="#111827",
        fg="white"
    )
    etiqueta_minimo.pack()

    entrada_minimo = tk.Entry(
        ventana_rango,
        font=("Arial", 13),
        justify="center"
    )
    entrada_minimo.pack(
        pady=(5, 20)
    )

    etiqueta_maximo = tk.Label(
        ventana_rango,
        text="Valor máximo:",
        font=("Arial", 12),
        bg="#111827",
        fg="white"
    )
    etiqueta_maximo.pack()

    entrada_maximo = tk.Entry(
        ventana_rango,
        font=("Arial", 13),
        justify="center"
    )
    entrada_maximo.pack(
        pady=(5, 25)
    )

    boton_continuar = tk.Button(
        ventana_rango,
        text="CONTINUAR",
        font=("Arial", 12, "bold"),
        width=20,
        command=lambda: validar_rango_grafico(
            ventana_modo,
            ventana_rango,
            entrada_minimo,
            entrada_maximo
        )
    )
    boton_continuar.pack()


def validar_rango_grafico(
    ventana_modo,
    ventana_rango,
    entrada_minimo,
    entrada_maximo
):
    try:
        minimo = int(
            entrada_minimo.get()
        )

        maximo = int(
            entrada_maximo.get()
        )

        if minimo >= maximo:
            messagebox.showerror(
                "Rango inválido",
                "El valor mínimo debe ser menor que el máximo."
            )
            return

        ventana_principal = (
            ventana_modo.master
        )

        ventana_rango.destroy()
        ventana_modo.destroy()

        abrir_partida_grafica(
            ventana_principal,
            minimo,
            maximo,
            "Personalizado"
        )

    except ValueError:
        messagebox.showerror(
            "Dato inválido",
            "Debes ingresar números enteros."
        )


def abrir_seleccion_modo(
    ventana_principal
):
    ventana_modo = tk.Toplevel(
        ventana_principal
    )

    ventana_modo.title(
        "Seleccionar modo"
    )

    ventana_modo.geometry(
        "500x520"
    )

    ventana_modo.resizable(
        False,
        False
    )

    ventana_modo.configure(
        bg="#111827"
    )

    titulo = tk.Label(
        ventana_modo,
        text="SELECCIONA UN MODO",
        font=("Arial", 22, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(45, 10)
    )

    descripcion = tk.Label(
        ventana_modo,
        text="Elige el nivel de dificultad",
        font=("Arial", 12),
        bg="#111827",
        fg="#cbd5e1"
    )
    descripcion.pack(
        pady=(0, 35)
    )

    boton_clasico = tk.Button(
        ventana_modo,
        text="CLÁSICO\nRango: 1 - 100",
        font=("Arial", 12, "bold"),
        width=25,
        height=3,
        command=lambda: seleccionar_modo_grafico(
            ventana_modo,
            1,
            100,
            "Clásico"
        )
    )
    boton_clasico.pack(
        pady=8
    )

    boton_experto = tk.Button(
        ventana_modo,
        text="EXPERTO\nRango: 1 - 1000",
        font=("Arial", 12, "bold"),
        width=25,
        height=3,
        command=lambda: seleccionar_modo_grafico(
            ventana_modo,
            1,
            1000,
            "Experto"
        )
    )
    boton_experto.pack(
        pady=8
    )

    boton_personalizado = tk.Button(
        ventana_modo,
        text="PERSONALIZADO",
        font=("Arial", 12, "bold"),
        width=25,
        height=3,
        command=lambda: abrir_rango_personalizado(
            ventana_modo
        )
    )
    boton_personalizado.pack(
        pady=8
    )

    boton_volver = tk.Button(
        ventana_modo,
        text="VOLVER",
        font=("Arial", 11),
        width=18,
        command=ventana_modo.destroy
    )
    boton_volver.pack(
        pady=25
    )

def abrir_estadisticas(ventana_principal):
    from datos import cargar_estadisticas

    estadisticas = cargar_estadisticas()

    ventana_estadisticas = tk.Toplevel(
        ventana_principal
    )

    ventana_estadisticas.title(
        "Estadísticas"
    )

    ventana_estadisticas.geometry(
        "560x620"
    )

    ventana_estadisticas.resizable(
        False,
        False
    )

    ventana_estadisticas.configure(
        bg="#111827"
    )

    titulo = tk.Label(
        ventana_estadisticas,
        text="ESTADÍSTICAS",
        font=("Arial", 24, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(40, 10)
    )

    subtitulo = tk.Label(
        ventana_estadisticas,
        text="Resumen de tus partidas",
        font=("Arial", 12),
        bg="#111827",
        fg="#94a3b8"
    )
    subtitulo.pack(
        pady=(0, 30)
    )

    historial = estadisticas.get(
        "historial",
        []
    )

    partidas_con_intentos = [
        partida
        for partida in historial
        if partida.get("intentos") is not None
    ]

    if partidas_con_intentos:
        total_intentos_historial = sum(
            partida["intentos"]
            for partida in partidas_con_intentos
        )

        promedio_intentos = (
            total_intentos_historial
            / len(partidas_con_intentos)
        )
    else:
        promedio_intentos = 0

    mejor_intentos = estadisticas.get(
        "mejor_intentos"
    )

    if mejor_intentos is None:
        mejor_intentos_texto = "Sin datos"
    else:
        mejor_intentos_texto = (
            f"{mejor_intentos} intento(s)"
        )

    marco_datos = tk.Frame(
        ventana_estadisticas,
        bg="#1e293b",
        padx=30,
        pady=25
    )
    marco_datos.pack(
        padx=50,
        fill="x"
    )

    datos = [
        (
            "Partidas registradas",
            estadisticas.get(
                "partidas",
                0
            )
        ),
        (
            "Partidas completadas",
            estadisticas.get(
                "completadas",
                0
            )
        ),
        (
            "Contradicciones",
            estadisticas.get(
                "contradicciones",
                0
            )
        ),
        (
            "Mejor resultado",
            mejor_intentos_texto
        ),
        (
            "Mejor puntaje",
            f"{estadisticas.get('mejor_puntaje', 0)} puntos"
        ),
        (
            "Promedio de intentos",
            f"{promedio_intentos:.2f}"
        )
    ]

    for nombre, valor in datos:
        fila = tk.Frame(
            marco_datos,
            bg="#1e293b"
        )
        fila.pack(
            fill="x",
            pady=10
        )

        etiqueta_nombre = tk.Label(
            fila,
            text=nombre,
            font=("Arial", 12),
            bg="#1e293b",
            fg="#cbd5e1"
        )
        etiqueta_nombre.pack(
            side="left"
        )

        etiqueta_valor = tk.Label(
            fila,
            text=str(valor),
            font=("Arial", 12, "bold"),
            bg="#1e293b",
            fg="white"
        )
        etiqueta_valor.pack(
            side="right"
        )

    boton_volver = tk.Button(
        ventana_estadisticas,
        text="VOLVER",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=ventana_estadisticas.destroy
    )
    boton_volver.pack(
        pady=35
    )

def abrir_detalle_partida(
    ventana_historial,
    partida,
    numero_partida
):
    ventana_detalle = tk.Toplevel(
        ventana_historial
    )

    ventana_detalle.title(
        f"Detalle de partida #{numero_partida}"
    )

    ventana_detalle.geometry(
        "520x600"
    )

    ventana_detalle.resizable(
        False,
        False
    )

    ventana_detalle.configure(
        bg="#111827"
    )

    titulo = tk.Label(
        ventana_detalle,
        text=f"PARTIDA #{numero_partida}",
        font=("Arial", 22, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(30, 10)
    )

    numero_adivinado = partida.get(
        "numero_adivinado"
    )

    if numero_adivinado is None:
        numero_adivinado = "No encontrado"

    resultado = partida.get(
        "resultado",
        "Sin datos"
    ).capitalize()

    informacion = (
        f"Rango: "
        f"{partida.get('rango_minimo', '-')}"
        f" - "
        f"{partida.get('rango_maximo', '-')}\n"
        f"Número: {numero_adivinado}\n"
        f"Intentos: {partida.get('intentos', 0)}\n"
        f"Puntaje: {partida.get('puntaje', 0)} puntos\n"
        f"Resultado: {resultado}"
    )

    etiqueta_info = tk.Label(
        ventana_detalle,
        text=informacion,
        font=("Arial", 12),
        justify="left",
        bg="#111827",
        fg="#cbd5e1"
    )
    etiqueta_info.pack(
        pady=(10, 25)
    )

    titulo_intentos = tk.Label(
        ventana_detalle,
        text="DETALLE DE INTENTOS",
        font=("Arial", 14, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo_intentos.pack(
        pady=(5, 10)
    )

    lista_intentos = tk.Listbox(
        ventana_detalle,
        width=48,
        height=15,
        font=("Arial", 11),
        bg="#1e293b",
        fg="white",
        selectbackground="#334155",
        borderwidth=0,
        highlightthickness=0
    )
    lista_intentos.pack(
        padx=30,
        pady=5
    )

    detalle = partida.get(
        "detalle_intentos",
        []
    )

    if not detalle:
        lista_intentos.insert(
            tk.END,
            "No existe detalle de intentos para esta partida."
        )

    else:
        for registro in detalle:
            respuesta = registro.get(
                "respuesta",
                ""
            )

            if respuesta == "mayor":
                texto_respuesta = "↑ Mayor"

            elif respuesta == "menor":
                texto_respuesta = "↓ Menor"

            elif respuesta == "correcto":
                texto_respuesta = "✓ Correcto"

            else:
                texto_respuesta = respuesta

            texto = (
                f"Intento #{registro.get('intento', '-')}"
                f"   |   "
                f"Número: {registro.get('numero', '-')}"
                f"   |   "
                f"{texto_respuesta}"
            )

            lista_intentos.insert(
                tk.END,
                texto
            )

    boton_cerrar = tk.Button(
        ventana_detalle,
        text="CERRAR",
        font=("Arial", 11, "bold"),
        width=18,
        height=2,
        command=ventana_detalle.destroy
    )
    boton_cerrar.pack(
        pady=25
    )


def abrir_historial(ventana_principal):
    from datos import cargar_estadisticas

    estadisticas = cargar_estadisticas()

    historial = estadisticas.get(
        "historial",
        []
    )

    ventana_historial = tk.Toplevel(
        ventana_principal
    )

    ventana_historial.title(
        "Historial de partidas"
    )

    ventana_historial.geometry(
        "760x700"
    )

    ventana_historial.resizable(
        False,
        False
    )

    ventana_historial.configure(
        bg="#111827"
    )

    titulo = tk.Label(
        ventana_historial,
        text="HISTORIAL DE PARTIDAS",
        font=("Arial", 24, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(30, 5)
    )

    subtitulo = tk.Label(
        ventana_historial,
        text=f"Partidas guardadas: {len(historial)}",
        font=("Arial", 12),
        bg="#111827",
        fg="#94a3b8"
    )
    subtitulo.pack(
        pady=(0, 20)
    )

    contenedor = tk.Frame(
        ventana_historial,
        bg="#111827"
    )
    contenedor.pack(
        fill="both",
        expand=True,
        padx=35
    )

    canvas = tk.Canvas(
        contenedor,
        bg="#111827",
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
        contenedor,
        orient="vertical",
        command=canvas.yview
    )

    marco_partidas = tk.Frame(
        canvas,
        bg="#111827"
    )

    marco_partidas.bind(
        "<Configure>",
        lambda evento: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    ventana_marco = canvas.create_window(
        (0, 0),
        window=marco_partidas,
        anchor="n"
    )


    def ajustar_ancho_historial(evento):
        canvas.itemconfig(
            ventana_marco,
            width=evento.width
        )


    canvas.bind(
        "<Configure>",
        ajustar_ancho_historial
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    if not historial:
        mensaje = tk.Label(
            marco_partidas,
            text="Todavía no existen partidas guardadas.",
            font=("Arial", 13),
            bg="#111827",
            fg="#cbd5e1"
        )
        mensaje.pack(
            pady=60
        )

    else:
        for indice, partida in enumerate(
            reversed(historial),
            start=1
        ):
            numero_real = (
                len(historial)
                - indice
                + 1
            )

            marco_partida = tk.Frame(
                marco_partidas,
                bg="#1e293b",
                padx=20,
                pady=15
            )
            marco_partida.pack(
                fill="x",
                pady=8,
                padx=90
            )

            encabezado = tk.Label(
                marco_partida,
                text=f"Partida #{numero_real}",
                font=("Arial", 13, "bold"),
                bg="#1e293b",
                fg="white"
            )
            encabezado.grid(
                row=0,
                column=0,
                sticky="w",
                pady=(0, 8)
            )

            numero = partida.get(
                "numero_adivinado"
            )

            if numero is None:
                numero = "-"

            resultado = partida.get(
                "resultado",
                "Sin datos"
            ).capitalize()

            informacion = (
                f"Rango: "
                f"{partida.get('rango_minimo', '-')}"
                f" - "
                f"{partida.get('rango_maximo', '-')}\n"
                f"Número: {numero}    "
                f"Intentos: {partida.get('intentos', 0)}\n"
                f"Puntaje: {partida.get('puntaje', 0)}    "
                f"Resultado: {resultado}"
            )

            etiqueta_datos = tk.Label(
                marco_partida,
                text=informacion,
                font=("Arial", 11),
                justify="left",
                bg="#1e293b",
                fg="#cbd5e1"
            )
            etiqueta_datos.grid(
                row=1,
                column=0,
                sticky="w"
            )

            boton_detalle = tk.Button(
                marco_partida,
                text="VER DETALLE",
                font=("Arial", 10, "bold"),
                width=14,
                command=lambda p=partida, n=numero_real: (
                    abrir_detalle_partida(
                        ventana_historial,
                        p,
                        n
                    )
                )
            )
            boton_detalle.grid(
                row=0,
                column=1,
                rowspan=2,
                padx=(40, 5)
            )

    boton_volver = tk.Button(
        ventana_historial,
        text="VOLVER",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        command=ventana_historial.destroy
    )
    boton_volver.pack(
        pady=20
    )

def mostrar_menu_grafico():
    ventana = tk.Tk()

    ventana.title(
        "Adivina el Número"
    )

    ventana.geometry(
        "600x650"
    )

    ventana.resizable(
        False,
        False
    )

    ventana.configure(
        bg="#111827"
    )

    titulo = tk.Label(
        ventana,
        text="ADIVINA EL NÚMERO",
        font=("Arial", 26, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(
        pady=(60, 10)
    )

    subtitulo = tk.Label(
        ventana,
        text="¿Podrá el computador leer tu mente?",
        font=("Arial", 13),
        bg="#111827",
        fg="#cbd5e1"
    )
    subtitulo.pack(
        pady=(0, 50)
    )

    boton_nueva = tk.Button(
        ventana,
        text="NUEVA PARTIDA",
        font=("Arial", 13, "bold"),
        width=25,
        height=2,
        command=lambda: abrir_seleccion_modo(
            ventana
        )
    )
    boton_nueva.pack(
        pady=8
    )

    boton_estadisticas = tk.Button(
        ventana,
        text="ESTADÍSTICAS",
        font=("Arial", 13),
        width=25,
        height=2,
        command=lambda: abrir_estadisticas(
            ventana
        )
    )
    boton_estadisticas.pack(
        pady=8
    )

    boton_historial = tk.Button(
        ventana,
        text="HISTORIAL",
        font=("Arial", 13),
        width=25,
        height=2,
        command=lambda: abrir_historial(
            ventana
        )
    )
    boton_historial.pack(
        pady=8
    )

    boton_ayuda = tk.Button(
        ventana,
        text="¿CÓMO JUGAR?",
        font=("Arial", 13),
        width=25,
        height=2,
        command=mostrar_como_jugar
    )
    boton_ayuda.pack(
        pady=8
    )

    boton_salir = tk.Button(
        ventana,
        text="SALIR",
        font=("Arial", 13),
        width=25,
        height=2,
        command=ventana.destroy
    )
    boton_salir.pack(
        pady=8
    )

    pie = tk.Label(
        ventana,
        text="Juego desarrollado en Python",
        font=("Arial", 10),
        bg="#111827",
        fg="#64748b"
    )
    pie.pack(
        side="bottom",
        pady=20
    )

    ventana.mainloop()


if __name__ == "__main__":
    mostrar_menu_grafico()