#####
#Realizar un Request
#Realizar una peticion a una API a python
#####

###1.- Sin dependencias
#Primero importamos la libreririas que necesitamos

#urllib.request nos sirve para obtener la informacion de la Api
import urllib.error
import urllib.request
import json

api_post = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_post)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
    response.close()
except urllib.error.URLError as e:
    print(f"Error en la solicitud {e}")
    
#Tray errro es para capturar los errores que salen al intentar la conexion

#2.- Con dependencias (requests)
import requests
print("\nGet: ")

api_post = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_post)
json_data = response.json()

print(json_data[0])

#3.- Podemos realizar un post
print("\nPOST: ")

api_post = "https://jsonplaceholder.typicode.com/posts"
input = {
    "userId": 1123,    
    "title": "Pruebas",
    "body": "Hola Mundo"
}
response = requests.post(api_post,json=input)
print(response.json())