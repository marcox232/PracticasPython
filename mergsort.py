#Merg Sort
#Algoritmo de ordenamiento recursivo

num_list = [2, 17, 8, 25, 12, 4, 29, 1, 19, 7]

def merg(list_izq,list_der):
    arr_result = []
    while len(list_izq) > 0 and len(list_der) > 0:
        if list_izq[0] > list_der[0]:
            arr_result.append(list_der[0])
            list_der.pop(0)
        else:
            arr_result.append(list_izq[0])
            list_izq.pop(0)
    
    while len(list_izq) > 0:
        arr_result.append(list_izq[0])
        list_izq.pop(0)
    
    while len(list_der) > 0:
        arr_result.append(list_der[0])
        list_der.pop(0)
    
    return arr_result

def mersort(listado):
    if len(listado) == 1:
        return listado
    
    mitad = len(listado) // 2 
    left_array = listado[:mitad]
    right_array = listado[mitad:]

    sorted_left_array = mersort(left_array)
    sorted_right_array = mersort(right_array)  

    return merg(sorted_left_array,sorted_right_array)

print(mersort(num_list))