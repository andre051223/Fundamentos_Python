#Condicionales

#IF -> Si se cumple la condicion, se ejecuta el bloque de codigo
#Else -> Si no se cumple la primera condicion, se ejecuta ese bloque de codigo (Se escribe fuera de la identacion del if)

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Condición Else-If (Elif) -> Si no se cumple la primera condicion, se evalua la segunda condicion, si se cumple, se ejecuta ese bloque de codigo
#Si no se cumple ninguna de las condiciones, se ejecuta el bloque de codigo del else

ingreso_mensual = 7000
if ingreso_mensual > 6000:
    print("Eres una persona de altos ingresos")
elif ingreso_mensual < 6000:
    print("Eres una persona de bajos ingresos")
