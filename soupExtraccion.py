from bs4 import BeautifulSoup
import requests

url = 'https://www.apple.com/mx/shop/buy-mac/macbook-air'

response = requests.get(url)

if response.status_code == 200:
    print("Extraccion correcta")
    sopa = BeautifulSoup(response.text,'html.parser')
    #print(sopa.prettify())
    
    title_tag = sopa.title
    if title_tag:
        print(f"El titulo es {title_tag.text}")
        
    """ precio = sopa.find('span',class_='rc-prices-fullprice')
    if precio:
        print(f"El precio es: {precio.text}") """
    
    """ precio_gen = sopa.find_all('span',class_='rc-prices-fullprice')
    for precios in precio_gen:
        print(f"El precio es {precios}") """
        
    product_Gen = sopa.find_all(class_='rc-productselection-item')
    for producto in product_Gen:
        espesificacion = producto.find(class_='rc-productbundle-title').text
        precio = producto.find(class_='rc-prices-fullprice').text
        
        print(f"Las espesificaciones son:{espesificacion}\n\nel precio es: {precio}\n\n\n")