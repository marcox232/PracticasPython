#Quick Sort
#Intento de realizar este algoritmo de ordenamiento

#Esta es la segunda parte de la interaccion para el tema generar quickt_Sort

def quick_sort (lista,inicio,fin):
    if inicio < fin:
        
        #dividir y acomodar pivote
        pi = partition(lista,inicio,fin)
        
        quick_sort(lista,inicio,pi-1)
        quick_sort(lista,pi+1,fin)
   

#Empezamos con la parte del pibote, es partition se compone de 3 elementos el array incio y fin del arreglo 

def partition(lista,inicio,fin):
   
    #Usaremos el ultimo elemnto del array
    pi = lista[fin]

    #Ultimo mas bajo que el pivote
    indicador = inicio - 1

   
    for a in range(inicio,fin):
        if lista[a] < pi:
            indicador +=1
            temporal = lista[a]
            lista[a] = lista[indicador]
            lista[indicador] = temporal

    seg_temp = lista[indicador+1]
    lista[indicador+1] = lista[fin]
    lista[fin] = seg_temp

    return indicador+1




num_lista = [5,10,2,8,1,7,4,9,3,6]

print(num_lista)
quick_sort(num_lista,0,len(num_lista)-1)
print(num_lista)

