# Juego Adivina el Número

## Descripción

Programa desarrollado en Python en el que el computador intenta adivinar un número pensado por el usuario dentro de un rango definido.

## Problema analizado

El problema consiste en encontrar un número desconocido utilizando únicamente las respuestas del usuario: mayor, menor o correcto.

## Solución seleccionada

Se utiliza una estrategia basada en el punto medio del rango. Después de cada respuesta, el sistema elimina los valores que ya no pueden ser correctos.

Se consideraron otras alternativas, como generar números aleatorios o recorrerlos uno por uno, pero la reducción del rango permite aprovechar mejor la información proporcionada por el usuario.

## Funcionalidades

- Configurar el rango de números.
- Validar números enteros.
- Generar intentos.
- Responder mayor, menor o correcto.
- Ajustar el rango de búsqueda.
- Contar intentos.
- Detectar respuestas contradictorias.
- Guardar estadísticas.
- Mostrar el mejor resultado.
- Permitir jugar nuevamente.

## Estructuras lógicas utilizadas

Se utilizaron estructuras condicionales como:

- if
- elif
- else

Estas permiten tomar decisiones según las respuestas del usuario.

También se utilizaron ciclos while para repetir los intentos y las validaciones.

## Arquitectura

El sistema está dividido principalmente en:

- `main.py`: coordinación general.
- `interfaz.py`: interacción con el usuario.
- `juego.py`: lógica principal del juego.
- `datos.py`: almacenamiento de estadísticas.

## Relación con los diagramas

Los diagramas desarrollados anteriormente representan directamente el funcionamiento implementado en el código.

Por ejemplo:

- Generar intento → `calcular_intento()`
- Validar respuesta → `solicitar_respuesta()`
- Ajustar rango → `jugar_partida()`
- Repetir intentos → ciclo `while`
- Detectar contradicciones → comparación entre mínimo y máximo

## Ejecución

```bash
python src/main.py