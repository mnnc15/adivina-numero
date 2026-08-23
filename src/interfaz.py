import tkinter as tk
from tkinter import messagebox


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
    ventana_partida.geometry("700x650")
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
            text=f"Posibilidades restantes: {posibilidades}"
        )

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

            messagebox.showinfo(
                "¡Número encontrado!",
                f"¡Lo adiviné!\n\n"
                f"Tu número es: {intento}\n"
                f"Intentos: {estado['intentos']}\n"
                f"Puntaje: {puntaje} puntos",
                parent=ventana_partida
            )

            ventana_partida.destroy()
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


def abrir_rango_personalizado(ventana_modo):
    ventana_rango = tk.Toplevel(ventana_modo)

    ventana_rango.title("Rango personalizado")
    ventana_rango.geometry("420x400")
    ventana_rango.resizable(False, False)
    ventana_rango.configure(bg="#111827")

    titulo = tk.Label(
        ventana_rango,
        text="RANGO PERSONALIZADO",
        font=("Arial", 19, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(pady=(40, 30))

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
    entrada_minimo.pack(pady=(5, 20))

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
    entrada_maximo.pack(pady=(5, 25))

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
        minimo = int(entrada_minimo.get())
        maximo = int(entrada_maximo.get())

        if minimo >= maximo:
            messagebox.showerror(
                "Rango inválido",
                "El valor mínimo debe ser menor que el máximo."
            )
            return

        ventana_principal = ventana_modo.master

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


def abrir_seleccion_modo(ventana_principal):
    ventana_modo = tk.Toplevel(ventana_principal)

    ventana_modo.title("Seleccionar modo")
    ventana_modo.geometry("500x520")
    ventana_modo.resizable(False, False)
    ventana_modo.configure(bg="#111827")

    titulo = tk.Label(
        ventana_modo,
        text="SELECCIONA UN MODO",
        font=("Arial", 22, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(pady=(45, 10))

    descripcion = tk.Label(
        ventana_modo,
        text="Elige el nivel de dificultad",
        font=("Arial", 12),
        bg="#111827",
        fg="#cbd5e1"
    )
    descripcion.pack(pady=(0, 35))

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
    boton_clasico.pack(pady=8)

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
    boton_experto.pack(pady=8)

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
    boton_personalizado.pack(pady=8)

    boton_volver = tk.Button(
        ventana_modo,
        text="VOLVER",
        font=("Arial", 11),
        width=18,
        command=ventana_modo.destroy
    )
    boton_volver.pack(pady=25)
    

def mostrar_menu_grafico():
    ventana = tk.Tk()

    ventana.title("Adivina el Número")
    ventana.geometry("600x650")
    ventana.resizable(False, False)
    ventana.configure(bg="#111827")

    titulo = tk.Label(
        ventana,
        text="ADIVINA EL NÚMERO",
        font=("Arial", 26, "bold"),
        bg="#111827",
        fg="white"
    )
    titulo.pack(pady=(60, 10))

    subtitulo = tk.Label(
        ventana,
        text="¿Podrá el computador leer tu mente?",
        font=("Arial", 13),
        bg="#111827",
        fg="#cbd5e1"
    )
    subtitulo.pack(pady=(0, 50))

    boton_nueva = tk.Button(
        ventana,
        text="NUEVA PARTIDA",
        font=("Arial", 13, "bold"),
        width=25,
        height=2,
        command=lambda: abrir_seleccion_modo(ventana)
    )
    boton_nueva.pack(pady=8)

    boton_estadisticas = tk.Button(
        ventana,
        text="ESTADÍSTICAS",
        font=("Arial", 13),
        width=25,
        height=2,
        command=lambda: messagebox.showinfo(
            "Estadísticas",
            "Aquí mostraremos las estadísticas del jugador."
        )
    )
    boton_estadisticas.pack(pady=8)

    boton_historial = tk.Button(
        ventana,
        text="HISTORIAL",
        font=("Arial", 13),
        width=25,
        height=2,
        command=lambda: messagebox.showinfo(
            "Historial",
            "Aquí mostraremos las partidas anteriores."
        )
    )
    boton_historial.pack(pady=8)

    boton_ayuda = tk.Button(
        ventana,
        text="CÓMO JUGAR",
        font=("Arial", 13),
        width=25,
        height=2,
        command=mostrar_como_jugar
    )
    boton_ayuda.pack(pady=8)

    boton_salir = tk.Button(
        ventana,
        text="SALIR",
        font=("Arial", 13),
        width=25,
        height=2,
        command=ventana.destroy
    )
    boton_salir.pack(pady=8)

    pie = tk.Label(
        ventana,
        text="Juego desarrollado en Python",
        font=("Arial", 10),
        bg="#111827",
        fg="#64748b"
    )
    pie.pack(side="bottom", pady=20)

    ventana.mainloop()


if __name__ == "__main__":
    mostrar_menu_grafico()