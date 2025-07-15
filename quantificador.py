#
#Quantificadores
#

#Importal Libreria
import re

#*
#Comodin de que puede aparecer 0 o mas veces
texto = "aaaba"
pattern = r"a*"

result = re.findall(pattern,texto)
print(result) #['aaa', '', 'a', '']

#+
#Si existe 1 o mas veces
texto = "aaaba"
pattern = r"a+"

result = re.findall(pattern,texto)
print(result) #['aaa', 'a']

#?
#En cuentre cero o 1 vez la letra
texto = "aaaabacb"
pattern = r"a?b"

result = re.findall(pattern,texto)
print(result) #['ab', 'b']

#{n}
#Encontrar n veces la letra o simbolo
texto = "aaaaaa aa aaa a aaaa"
pattern = r"a{3}"

result = re.findall(pattern,texto)
print(result)  #['aaa', 'aaa', 'aaa', 'aaa']

#{n,m}
#Busca minumo n a maximo m
texto = "uu u uuu uuuu u"
pattern = r"u{2,3}"

result = re.findall(pattern,texto)
print(result) #['uu', 'uuu', 'uuu']