#Los metodos de listas son funciones aplicadas a objetos, en este caso listas
# Recordar que las listas se definen con corchetes []

#list
jugadores = list(["Messi", "Xavi", "Iniesta", "Puyol"])
print(jugadores)
print(jugadores[0])
print(jugadores[1])
print(jugadores[2])
print(jugadores[3])

#insert: Inserta un elemento en una posicion especifica
jugadores.insert(1, "Busquets") #Inserta "Busquets" en la posicion 1
print(jugadores)

#append: Agrega un elemento al final de la lista
jugadores.append("Alba") #Agrega "Alba" al final de la lista
print(jugadores)

#extend: Agrega los elementos de una lista al final de otra lista
nuevosJugadores = ["Dembélé", "Griezmann", "Suárez"]
jugadores.extend(nuevosJugadores) #Agrega los elementos de la lista nuevos jugadores al final de la lista jugadores
print(jugadores)

#pop: Elimina un elemento de la lista en una posicion especifica y lo devuelve
jugadorEliminado = jugadores.pop(2) #Elimina el elemento en la posicion 2 y lo devuelve
print("Jugador eliminado: ", jugadorEliminado)
print(jugadores)

#remove: Elimina la primera ocurrencia de un elemento en la lista
jugadores.remove("Puyol") #Elimina la primera ocurrencia de "Puyol"
print(jugadores)

#sort: Ordena los elementos de la lista en orden alfabetico
jugadores.sort() #Ordena los elementos de la lista en orden alfabetico
print(jugadores)

#reverse: Invierte el orden de los elementos de la lista
jugadores.reverse() #Invierte el orden de los elementos de la lista
print(jugadores)

#clear: Elimina todos los elementos de la lista
#jugadores.clear() #Elimina todos los elementos de la lista
#print(jugadores)

#tamaño de la lista
tamañoLista = len(jugadores) #Devuelve el tamaño de la lista
print("Tamaño de la lista: ", tamañoLista)
