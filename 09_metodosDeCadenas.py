# Los metodos son funciones aplicadas a objetos, en este caso cadenas de texto
# Recordar que los espacios cuentan como caracteres

cadena1 = "fc barcelona"
cadena2 = "més que un club"
cadena3 = "12345"
cadena4 = "123a45"


resultado1 = cadena1.upper() # Convierte la cadena a mayusculas
resultado2 = cadena2.lower() # Convierte la cadena a minusculas
resultado3 = cadena1.capitalize() #Convierte la primera letra en mayuscula
resultado4 = cadena2.title() #Convierte la primera letra de cada palabra en mayuscula

#metodo find
posicion = cadena1.find("bar") #Busca la posicion de la subcadena "bar"

#busqueda de una cadena en otra cadena
posicion = cadena1.find("bar", posicion)
posicion1 = cadena1.find("z") #Si no encuentra la subcadena, devuelve -1

#metodo isNumeric
resultado5 = cadena3.isnumeric()  #Devuelve True porque solo contiene numeros
resultado6 = cadena4.isnumeric() #Devuelve False porque contiene una letra

#contar coincidencias
coincidencias = cadena1.count("a") #Cuenta cuantas veces aparece la letra "a" en la cadena1

#contar cantidad de caracteres
cantidadCaracteres = len(cadena1) #Cuenta la cantidad de caracteres en la cadena1
cantidadCaracteres2 = len(cadena2) #Cuenta la cantidad de caracteres en la cadena

#empezar con caracter especifico
empiezaCon = cadena1.startswith("f") #Devuelve True si la cadena1 empieza con "f"
empiezaCon2 = cadena2.startswith("f") #Devuelve False si la cadena2 no empieza con "f"

#terminar con caracter especifico
terminaCon = cadena1.endswith("a") #Devuelve True si la cadena1 termina con "a"
terminaCon2 = cadena2.endswith("a") #Devuelve False si la cadena2 no termina con "a"

#replace: #Reemplaza una subcadena por otra
cadenaReemplazada = cadena1.replace("barcelona", "madrid") #Reemplaza "barcelona" por "madrid"

#strip: Elimina los espacios en blanco al inicio y al final de la cadena
cadenaConEspacios = "   Hola Mundo   "
cadenaSinEspacios = cadenaConEspacios.strip() #Elimina los espacios en blanco al inicio y al final

print(dir(cadena1)) # Muestra todos los metodos disponibles para cadenas de texto
print(dir(cadena2)) # Muestra todos los metodos disponibles para cadenas de texto

print(resultado1)
print(resultado2)
print(resultado3)
print(resultado4)
print("La posicion de la subcadena 'bar' en la cadena1 es: ", posicion)
print(posicion)
print(posicion1)
print("La cadena3 es numerica: ", resultado5)
print("La cadena4 es numerica: ", resultado6)
print("La letra 'a' aparece ", coincidencias, " veces en la cadena1")
print(cantidadCaracteres)
print(cantidadCaracteres2)
print(empiezaCon)
print(empiezaCon2)
print(terminaCon)
print(terminaCon2)
print(cadenaReemplazada)
print("Cadena con espacios: '", cadenaConEspacios, "'")
print("Cadena sin espacios: '", cadenaSinEspacios, "'")