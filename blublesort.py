#Bubble Sort
#Algoritmo de ordenamiento

list_num = [3,8,5,9,7,1,4]

print(list_num)

def orde_bubble_sort(lista):
    
    for a in range(len(lista)):
        for b in range(len(lista)-a-1):
            
            if lista[b] > lista[b+1]:
                temp = lista[b]
                lista[b] = lista[b+1]
                lista[b+1] = temp
    print(lista)



orde_bubble_sort(list_num)