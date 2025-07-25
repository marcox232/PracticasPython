#Scraping
#Podre extraer informacion de otras paginas para el uso o benificio

import requests
import re

url = 'https://www.apple.com/mx/shop/buy-mac/macbook-air'

response = requests.get(url)

if response.status_code == 200:
    print("Peticion Existosa")
    
    html = response.text
    #print(html)
    
    #Realizar una expresion regular
    price_patterne = r'<span class="rc-prices-fullprice">(.*?)</span>'
    resultados = re.search(price_patterne,html)
    
    if resultados:
        print(f"El precio del producto {resultados.group(1)}")
        

from bs4 import BeautifulSoup
import requests

url = 'https://www.apple.com/mx/shop/buy-mac/macbook-air'

response = requests.get(url)

if response.status_code == 200:
    print("Extraccion correcta")
    sopa = BeautifulSoup(response.text,'html.parser')
