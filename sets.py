#Set y Corchetes

#Importamos libreria
import re

#[]
#Coincide con cualquier caracter dentro de los corchetes
user_name = "rub.$ius_69+"

pattern_1 = r"^[\w._%\+\-]+$"

resul_1 = re.search(pattern_1,user_name)
print(resul_1)

pattern_2 = r"^[\w.\$%\+\-]+$"
resul_2 = re.search(pattern_2,user_name)
print(resul_2)

#Eejmplo: Encontra todas la vocales
texto = "Hola mundo"
pattern =r"[aeiou]"

result = re.findall(pattern,texto)
print(result)

#Ehmplo: Como encontrar palabras espesificas, man fan y ban
texto = "man ran fan pan ban omniman"
pattern = r"\b[mfb]an\b"

result = re.findall(pattern,texto)
print(result)

#[r-m]
#Podemos colocar rangos para encontrar conincidencias
#[a-z]
#[A-Z]
#[0-9]
#Tambien se puede combinar rangos
#[a-zA-Z]
#[0-9A-Z]

#Ejmplo: Solo letras sin ningun numero
nombre = "Marco"
apellido = "rodriguez"
ubicacion = "priv 8"

pattern = r"^[a-z]{1,}$"
print(re.findall(pattern,nombre))
print(re.findall(pattern,apellido))
print(re.findall(pattern,ubicacion))

#Ejercicio practivo, generar un Regular expresion para Email

correo_1 = "michael@gov.co.uk"

pattern = r"^[\w._%+-]+@[\w.-]+\.([a-zA-Z]{2,10}|[a-zA-Z]{2,10}\.[a-zA-Z]{2,4})$"

result = re.search(pattern,correo_1)
if result: print(f"Correo Correcto {result.group()}")
else: print("Correo Incorrecto")

#[^]
#Negacion lo que este ddentro no lo tomara en cuenta

texto = "Hola Mundo"
pattern = r"[^aeiou]"

result = re.findall(pattern,texto)
print(result)

