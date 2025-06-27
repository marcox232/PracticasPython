#Practica para aprender python 
#Ejercicio numero 1 peleas de listados, la idea genera el recibir 2 listados de numeros 
#Compararlo por posicion y quien se mas grande gana y lo que sobre se pasa al segundo, se compara y en caso de que quedar empate no se pasa nada 
#Al final gana quien mas puntos tenga y se debe pasar la cantidad de cuanto fue de lo que sobro.
#En caso de empate se manda la leyenda empate

lista_a = [5,3,2]
lista_b = [3,2,7]

def comparacion_listas(lista_a,lista_b):
    contador_a = 0
    contador_b = 0
    
    for a in range(len(lista_a)):
        print(f"Lista a {(lista_a[a]+contador_a)} Lista b {(lista_b[a]+contador_b)}")
        if (lista_a[a]+contador_a) > (lista_b[a]+contador_b):
            contador_a = (lista_a[a]+contador_a) - (lista_b[a]+contador_b)
        elif (lista_a[a]+contador_a) < (lista_b[a]+contador_b):
            contador_b = (lista_b[a]+contador_b) - (lista_a[a]+contador_a)
        else:
            contador_a = 0
            contador_b = 0

        print(f"Contador a {contador_a}, contador b {contador_b}")
    
    if contador_a > contador_b:
        print(f"A{contador_a}")
    elif contador_a < contador_b:
        print(f"B{contador_b}")
    else:
        print("Empate")   
        
        
comparacion_listas(lista_a,lista_b)