#Practicas Listas

lis_numeros = [1,3,9,5,2,6,8]

print(lis_numeros)

def ordenar_numeros (lista):
    
    for a in range(len(lista)):
        puntero = a
        for b in range(a+1,len(lista)):
            if lista[puntero] > lista[b]:
               puntero = b

        
        dato2 = lista[puntero]
        lista[puntero] = lista[a]
        lista[a] = dato2
           
    print(lista)
        
   
            


ordenar_numeros(lis_numeros)