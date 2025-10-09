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

#Ejemplo de tupla
tupla = (1, 2, 3, 4, 5)
print(tupla)
print(type(tupla)) #Muestra el tipo de dato de la variable