#String (Cadenas de texto)
nombre = "Diego"
apellido = "Lopez"
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)
print(type(nombre_completo))

#Datos Enteros
x=10
y=5
z=x+y
print("El resultado de la suma es:", z)
print(type(z))

#Datos Flotantes (Decimales)
a=3.5
b=2.5
c=a*b
print("El resultado de la multiplicación es:", c)
print(type(c))

#Datos Booleanos (True o False)
es_mayor = x > y
print("¿x es mayor que y?", es_mayor)
print(type(es_mayor))

#Booleanos (True o False)
es_menor = x < y
print("¿x es menor que y?", es_menor)
print(type(es_menor)) #Muestra el tipo de dato de la variable es_menor

#Datos compuestos (Listas, Tuplas, Diccionarios, Conjuntos)

#Listas
#Importante: el primer dato de una lista empieza en la posición 0
listaDeObjetivos = [
    "Aprender Fundamentos de Python",
    "Aprender Python Orientado a Objetos",
    "Aprender SQL y Bases de Datos",
    "Aprender Ecommerce",
    "Consolidarme en Castor Data",
    "Trabajar como AI Engineer en Perfila.Ai"
]
print(listaDeObjetivos)
print(type(listaDeObjetivos)) #Muestra el tipo de dato de la variable

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(listaNumeros)
print(type(listaNumeros)) #Muestra el tipo de dato de la variable

#Listas mixtas
listaMixta = ["Hola", 123, True, 45.67, False, "Mundo"]
print(listaMixta)
print(type(listaMixta)) #Muestra el tipo de dato de la variable

#Lista con posiciones especificas
listaPosiciones = [10, 20, 30, 40, 50]
print(listaPosiciones[0]) #Muestra el primer elemento de la lista
print(listaPosiciones[2]) #Muestra el tercer elemento de la lista
print(listaPosiciones[4]) #Muestra el quinto elemento de la lista
print(listaPosiciones[-1]) #Muestra el ultimo elemento de la lista
print(listaPosiciones[-3]) #Muestra el antepenultimo elemento de la lista
print(listaPosiciones[-5]) #Muestra el primer elemento de la lista
print(len(listaPosiciones)) #Muestra la cantidad de elementos de la lista


equipos_futbol = ["FC Barcelona", "Real Madrid", "Manchester United", "Bayern Munich"]
print(equipos_futbol)
print(type(equipos_futbol))

#listas sin memoria
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8, 9, 10]
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)
print(id(lista_1)) #Muestra la direccion de memoria de la lista_1
print(id(lista_2)) #Muestra la direccion de memoria de la lista_2

#Matrices y Tuplas
#Una matriz es una coleccion de datos organizados en filas y columnas
#Una tupla es una coleccion de datos inmutable, es decir, no se puede modificar
#Las tuplas se definen con parentesis ()
#Las matrices se definen con corchetes []
#Ejemplo de matriz

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matriz)
print(type(matriz)) #Muestra el tipo de dato de la variable

#Acceder a un elemento de la matriz
print(matriz[0][0]) #Muestra el primer elemento de la primera fila
print(matriz[1][2]) #Muestra el tercer elemento de la segunda fila
print(matriz[2][1]) #Muestra el segundo elemento de la tercera fila
print(matriz[-1][-1]) #Muestra el ultimo elemento de la ultima fila
print(matriz[-2][-3]) #Muestra el primer elemento de la segunda fila
print(matriz[-3][-2]) #Muestra el segundo elemento de la primera fila
print(len(matriz)) #Muestra la cantidad de filas de la matriz


#Tuplas
# A diferencia de las listas, las tuplas son inmutables, es decir, no se pueden modificar una vez creadas.
paises = ("España", "Inglaterra", "Alemania", "Italia")
print(paises)
print(type(paises))

#Diccionario
# Los diccionarios son colecciones de pares clave-valor.
jugador_1 = {
    "nombre": "Lionel Messi",
    "edad": 36,
    "equipo": "Inter Miami",
    "goles": 30
}

jugador_2 = {
    "nombre": "Cristiano Ronaldo",
    "edad": 39,
    "equipo": "Al Nassr",
    "goles": 25
}

jugador_3 = {
    "nombre": "Kylian Mbappé",
    "edad": 25,
    "equipo": "Real Madrid",
    "goles": 28
}

print(jugador_1)
print(type(jugador_1))
print(jugador_2)
print(type(jugador_2))
print(jugador_3)
print(type(jugador_3))