# Juego Adivina el Número

## Nombre del proyecto

**Juego Adivina el Número**

## Integrante

- **Mathias Nicolás Núñez Córdova**

## Objetivo del sistema

Desarrollar un juego en Python en el que el computador intente adivinar un número pensado por el usuario dentro de un rango determinado, aplicando estructuras de programación como funciones, condicionales, ciclos, validaciones y manejo de datos.

El sistema utiliza las respuestas del jugador para reducir progresivamente el rango de posibilidades hasta encontrar el número correcto. Además, incorpora una interfaz gráfica y funcionalidades adicionales que permiten mejorar la experiencia del usuario y registrar el desarrollo de las partidas.

## Descripción de funcionalidades

El sistema cuenta con las siguientes funcionalidades:

- Menú principal mediante una interfaz gráfica desarrollada con **Tkinter**.
- Selección de diferentes modos de juego:
  - **Clásico:** rango de 1 a 100.
  - **Experto:** rango de 1 a 1000.
  - **Personalizado:** permite definir un rango propio.
- Validación del rango personalizado para comprobar que el valor mínimo sea menor que el valor máximo.
- Generación de intentos utilizando el valor intermedio del rango disponible.
- Opciones para indicar si el número pensado es:
  - Mayor.
  - Menor.
  - Correcto.
- Reducción progresiva del rango de búsqueda según las respuestas del usuario.
- Contador automático de intentos.
- Visualización del rango actual durante la partida.
- Visualización de las posibilidades restantes.
- Barra gráfica que representa cómo se reduce el espacio de búsqueda.
- Porcentaje de progreso de la búsqueda.
- Historial visual de los intentos realizados durante una partida.
- Registro del número propuesto y de la respuesta correspondiente a cada intento.
- Detección de respuestas contradictorias.
- Posibilidad de corregir la última respuesta cuando se detecta una contradicción.
- Restauración automática del estado anterior de la partida después de corregir una respuesta.
- Sistema de puntuación basado en el tamaño del rango y la cantidad de intentos utilizados.
- Pantalla final de victoria que muestra:
  - Número encontrado.
  - Cantidad de intentos.
  - Puntaje obtenido.
  - Máximo esperado de intentos.
  - Calificación mediante estrellas.
  - Valoración del desempeño.
- Opción para jugar nuevamente.
- Opción para regresar al menú principal.
- Registro permanente de estadísticas mediante un archivo JSON.
- Consulta de estadísticas generales:
  - Partidas registradas.
  - Partidas completadas.
  - Contradicciones.
  - Mejor cantidad de intentos.
  - Mejor puntaje.
  - Promedio de intentos.
- Historial general de partidas.
- Visualización del rango, número encontrado, cantidad de intentos, puntaje y resultado de cada partida.
- Opción **Ver detalle** para consultar todos los intentos realizados en una partida anterior.
- Sección **Cómo jugar** con instrucciones para el usuario.

## Fecha

**23 de agosto de 2026**