#En este caso veremos los metacaracteres de las expresciones regulares
#Son simbolos especiales con significados espesificos en los patrones regulares

import re

#1.- El punto (.)
#Coincidir con cualquier caracter a excepcion de una nuea linea

texto = "Hola mundo, H0la de nuevo, H9la por ultimo Hoola"
pattern = "H.la"

found = re.findall(pattern,texto)

print(found)

#La r hace mencion que es una exprecion regular

#Para encontrar el punto en un texto se utilizara la barra invertida para poder buscar el punto

texto = "Señor del silencio, el viento susurra promesas que el señor del olvido se llevó. en cada rincón, ecos perdidos buscan volver a ser memoria."
pattern = r"\."

found = re.findall(pattern,texto)
print(found)

#\d
#Coincide con cualquier digito del 0 al 9 un solo digito

texto = "Hola el numero de cuentas es 12347662647128368"
pattern = r"\d"

result = re.findall(pattern,texto)
print(result)

#En el caso de querer encontrar mas 1 numero puedo usar la exprecion de {9}. que hace mencion la cantidad de numeros que debe traer una vez encuente el primer digitos

texto = "Hola el numero de cuentas es 12347662647128368"
pattern = r"\d{17}"

result = re.findall(pattern,texto)
print(result)

#\w
#Coincide con cualquier caracter alfa numerico (a-z) (0-9). El guion bajo tambien lo reconoce

texto = "@@@marco_64#$!"
pattern = r"\w"

result = re.findall(pattern,texto)
print(result)

#\s
#Coicidencia con espacios, salto de linea y tabulaciones
texto = "Hola Mundo\n ¿Como Estas?\t"
pattern = r"\s"

result = re.findall(pattern,texto)
print(result)
#^
#El inicio de la cadena de texto debe empezar con el signo despues de este
user_name = "%marxo"
pattern = r"^\w"

validacion = re.search(pattern,user_name)

print(validacion)

#Valida numero de telefono
num_phone = "+55 87871238812"
pattern = r"^\+\d{1,3} "

valid = re.search(pattern,num_phone)
if valid: print("Numero de Telefono valido")
else: print("Numero de Telefono no valido")

#$
#El signo de pesos es para que la frase termine con lo que solicita
texto = "Hola Mundo."
pattern = r"Mundo$"

valid = re.search(pattern,texto)

if valid: print("Si termina con Mundo")
else: print("No termina")

#\b
#Buscar por palabra en espesifico
texto = "casa casada casado casa"
pattern = r"\bcasa\b"

result = re.findall(pattern,texto)
print(result)

#|
#Este permite agregar mas de una opcion en la validacion en general es un OR

texto = "Sandia, Platano, Aguacate, Pera, Palta"
pattern = r"Palta|Aguacate"

result = re.findall(pattern,texto)

print(result)