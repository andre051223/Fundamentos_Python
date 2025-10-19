# Los metodos de diccionarios son funciones aplicadas a objetos, en este caso diccionarios

plataforma = {
    "nombre": "perfila.ai",
    "tipo": "IA generativa",
    "CEO": "Michelle Engelmann",
    "fundacion": 2023,
}

plataforma_2 = {
    "nombre": "Platzi",
    "tipo": "Educacion en linea",
    "CEO": "Freddy Vega",
    "fundacion": 2011,
}

plataforma_3 = {
    "nombre": "edTeam",
    "tipo": "Educacion en linea",
    "CEO": "Javier Santaolalla",
    "fundacion": 2015,
}

#keys: Devuelve una lista con las claves del diccionario
claves = plataforma.keys()
claves_2 = plataforma_2.keys()
claves_3 = plataforma_3.keys()
print("Claves del diccionario: ", list(claves))
print("Claves del diccionario: ", list(claves_2))
print("Claves del diccionario: ", list(claves_3))

#get: Devuelve el valor de una clave especifica
valor = plataforma.get("nombre")
valor_2 = plataforma_2.get("nombre")
valor_3 = plataforma_3.get("nombre")

print("Valor de la clave 'nombre': ", valor)
print("Valor de la clave 'nombre': ", valor_2)
print("Valor de la clave 'nombre': ", valor_3)

#none: Devuelve None si la clave no existe
valor_none = plataforma.get("ubicacion")
print("Valor de la clave 'ubicacion': ", valor_none)

#clear: Elimina todos los elementos del diccionario
#plataforma.clear()
#print("Diccionario después de clear:"", plataforma)