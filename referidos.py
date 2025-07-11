#Esn este arhivo voy a practicar expreciones Regulares para entender el tema de busqueda

#Es importante importar la libreria
import re

texto = "Marco Antonio Rodriguez hola Bizarro"
pattern = "hola"

result = re.search(pattern, texto)

#Nos dice la palabra encontrada
print(result.group())

#No indica en que posicion inicia la palabra encontrada
print(result.start())

#Nos dice donde termina la palabra encontrada
print(result.end())
#Es el resultado genero si no es none el if lo toma como true 
print(result)

#Con .findall() nos mostrara todas las ocurrencias que el patron tiene en el texto

texto = "La vida es una travesía de sueños, desafíos y momentos efímeros que nos transforman. Aprendemos a caer, a levantarnos, a amar y a dejar ir. Cada paso que damos, cada elección, es parte del lienzo que pintamos. y aunque imperfecto, ese cuadro es profundamente nuestro."

pattern = "y"

resultado = re.findall(pattern,texto)
print(resultado)

#Con el comando .iter() nos traera una listado de resultados con la posicion de inicio y fin de toddas la conincidencias

texto = "En la penumbra del alma, el señor del tiempo avanza sin tregua. El señor de los recuerdos susurra promesas perdidas. Y el señor de los sueños, eterno guardián del anhelo, danza en la mente de quienes aún creen en lo imposible. Tres señores, tres destinos, un solo corazón buscando sentido."

pattern = "señor"

encontrados_list = re.finditer(pattern,texto)

for a in encontrados_list:
    print(f" {a.group()} - {a.start()} - {a.end()}")
    
#Modificadores

#Los modificadores son un atributo extra donde podemos ingresar para ya sea ingororar algun argumento o bien agregar algun filtro

#re.IGNORECASE sirve para no tomar en cuenta las mayusculas y minusculas del filtro o pattern

texto = "Señor del silencio, el viento susurra promesas que el señor del olvido se llevó. en cada rincón, ecos perdidos buscan volver a ser memoria."

pattern = "señor"

resultado = re.findall(pattern,texto,re.IGNORECASE)

print(resultado)

#.sub() permite realizar remplazo de palabras por la que coincidadn con el pattern
texto = "Señor del silencio, el viento susurra promesas que el señor del olvido se llevó. en cada rincón, ecos perdidos buscan volver a ser memoria."

pattern = "señor"

replacement = "Señora"

resultado = re.sub(pattern,replacement,texto)

print(resultado)

