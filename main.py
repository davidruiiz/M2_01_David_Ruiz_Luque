#1)Indica un ejemplo de un tipo de dato:

#entero
7
#flotante
3.141592
#string
"Hola"
#booleano  
Aprobado = True
Suspenso = False

#2) Crea dos variables que se llamen nombre y apellido, en ellas introduce tu nombre y apellidos y luego prueba lo siguiente e indica el resultado:

#Variable nombre:
nombre="David"
#Variable apellido:
apellidos="Ruiz Luque"

#nombre + apellido
print(nombre + apellidos)
#nombre + apellido + "."
print(nombre + apellidos + ".")
#nombre * 3
print(3*nombre)

#3) Retoma el ejercicio anterior, crea una variable que se llame nombreCompleto que una tu nombre y tu apellido con un espacio en el medio. Sobre esta variable, ¿eres capaz a extraer tu nombre utilizando slicing?

#Variable nombre completo:
nombreCompleto=(nombre + " " +apellidos)
print(nombreCompleto)
#Extraemos el nombre utilizando slicing:
print(nombreCompleto[0:5])