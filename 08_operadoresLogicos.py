# Los operadores logicos son 3 (And, Or, Not)
# Si las 2 condiciones son verdaderas, el resultado es verdadero
# Si una de las 2 condiciones es verdadera, el resultado es verdadero
# Si las 2 condiciones son falsas, el resultado es falso
# Si la condicion es verdadera, el resultado es falso
# Si la condicion es falsa, el resultado es verdadero
# Si la condicion es verdadera, el resultado es verdadero

#Ejemplo práctico

Escenario = True & True
Escenerio2 = True & False
Escenerio3 = False & True
Escenerio4 = False & False

print("Escenario 1 (True & True): ", Escenario)
print("Escenario 2 (True & False): ", Escenerio2)
print("Escenario 3 (False & True): ", Escenerio3)
print("Escenario 4 (False & False): ", Escenerio4)

