# Copilot-Instructions-Fundamentos-Python.md

## 🎯 Objetivo del Archivo

Este documento guía a **GitHub Copilot** para que sus sugerencias se adapten a un **nivel principiante-intermedio** en el aprendizaje de **los fundamentos de Python**. Las sugerencias deben enfocarse en fomentar la comprensión de la sintaxis, la lógica básica y las buenas prácticas, ofreciendo ejemplos simples, claros y comentados.

---

## 👩‍💻 Contexto de Aprendizaje

* Rol actual: **Frontend Developer** en transición hacia desarrollo backend.
* Objetivo actual: Comprender y practicar los **fundamentos de Python** para realizar scripts, automatizaciones y manipulación básica de datos.

---

## 🧠 Nivel de Conocimiento Esperado

* Nivel: **Principiante a intermedio**.
* El código sugerido debe ser **explicativo, con comentarios claros**.
* Se deben **evitar estructuras o librerías avanzadas**.
* Priorizar ejemplos ejecutables y prácticos.

---

## 💡 Recomendaciones de Estilo

1. Seguir la convención de nombres `snake_case` para variables y funciones.
2. Priorizar **legibilidad sobre optimización**.
3. Incluir **docstrings** y comentarios donde sea útil.
4. Mostrar ejemplos funcionales (entrada → proceso → salida).

---

## 🧩 Temas Prioritarios

1. **Sintaxis y estructura básica:** variables, tipos de datos, operadores.
2. **Control de flujo:** `if`, `elif`, `else`, bucles `for` y `while`.
3. **Funciones:** definición, parámetros, valores de retorno.
4. **Colecciones:** listas, tuplas, diccionarios, conjuntos.
5. **Manejo de errores:** `try`, `except`, `finally`.
6. **Módulos y librerías estándar:** `math`, `datetime`, `os`, `random`.
7. **Entrada/Salida:** lectura y escritura de archivos (`.txt`, `.csv`).
8. **Buenas prácticas básicas:** comentarios, legibilidad, organización de código.

---

## 🧩 Ejemplo de Interacción Esperada

> **Prompt:** "Crea una función que calcule el área de un triángulo a partir de su base y altura."
>
> **Respuesta esperada de Copilot:**
>
> ```python
> def calcular_area_triangulo(base, altura):
>     """Calcula el área de un triángulo dado su base y altura."""
>     area = (base * altura) / 2
>     return area
>
>
> base = 10
> altura = 5
> print(f"El área del triángulo es: {calcular_area_triangulo(base, altura)}")
> ```

---

## 🚀 Mini-Proyectos Recomendados

1. **Calculadora básica:** suma, resta, multiplicación, división.
2. **Conversor de unidades:** temperatura, monedas o distancias.
3. **Gestor de notas:** guardar y leer notas desde un archivo `.txt`.
4. **Juego simple:** adivinar el número aleatorio.
5. **Analizador de texto:** contar palabras, letras y frecuencia de caracteres.

---

## ✅ Objetivo Final

Dominar los fundamentos del lenguaje Python y preparar las bases para avanzar a **Programación Orientada a Objetos (POO)** y **SQL básico**.
