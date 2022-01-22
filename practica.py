arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]

print (arr)

arr = ["hola",3,5,7]
arr[0], arr[1] = arr[1], arr[0]

print (arr)

#Ordenamiento por seleccion 
arrX=[6,5,3,1,8,7,2,4]

def ordenamientoSeleccion(arrX):
    for i in range(len(arrX)):
        min=i
        for j in range(i,len(arrX)+1):
            if(arrX[j] < arrX[min]):
                min=j
        if(min != i):
            aux=arrX[i]
            arrX[i]=arrX[min]
            arrX[min]=aux
    print (arrX)
#Programa Principal

print (arrX)
ordenamientoSeleccion(arrX)