#
#Fechas en Pyton
#

#Importar librerias para fecha
from datetime import datetime, timedelta

#1.- Fecha y Hora actual
print(datetime.now())

#2.- Espesificar fecha y hora
spesific_date = datetime(2025, 9, 2, 20,18,3)
print(spesific_date)

#3.- Formato a la fecha
#Se utiliza el metodo strftime()
#En caso de querer como espesificar el formato se tiene que leer la documentacion de Python

format_date = spesific_date.strftime("%d/%m/%y")
print(format_date)

#El caso de las diagonales / solo se toma como texto se puede cambiar por cualquier cosa

format_date = spesific_date.strftime("%d - %m - %y")
print(format_date)

#4.- Sumar o Restar
#Pyton permite la suma y resta de dias horas segundos de manera sencilla

#Sumar
manana = datetime.now() + timedelta(days=1)
print(manana)

prox_semana = datetime.now() + timedelta(weeks=1)
print(prox_semana)

horas = datetime.now() + timedelta(hours=2)
print(horas)

#Restar
ayer = datetime.now() + timedelta(days=1)
print(ayer)

semana_pasada = datetime.now() + timedelta(weeks=1)
print(semana_pasada)

horas = datetime.now() + timedelta(hours=2)
print(horas)

#5.- Obtener datos diferentes a la fecha
hoy = datetime.now()

año_actual = hoy.year
mes_actual = hoy.month
dia_actual = hoy.day

print(f"El dia {dia_actual} del mes {mes_actual} del año {año_actual}")

#6.- Calculra diferencia de fechas

date1 = datetime.now()
date2 = datetime(2025, 9, 2, 3)

dias_cumple = date2 - date1
print(f"Falta para mi compleaños {dias_cumple}")

#7.- Cambiar la informacion de fechas a expañol
#Como se muestra orifinalmente
hoy = datetime.now()
format_date = hoy.strftime("%A/%B/%y")
print(format_date)

#Se tiene que importar otra libreria para obtener la informacion
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

hoy = datetime.now()
format_date = hoy.strftime("%A/%B/%y")
print(format_date)

