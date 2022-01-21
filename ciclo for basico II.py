# Tamaño Grande
from itertools import count


listaNum = [-1,-3,-5,6,7,9,2,-1,-4]
for i in listaNum:
    if i < 0:
        print("big")
    if i > 0:
        print(i)

#Contar Positivos 
listaNum = [-1,-3,-5,6,7,9,2,-1,-4]
listaPos=[]
for num in listaNum:
    if(num > 0):
        listaPos.append(num)
listaNum.append(len(listaPos))
print(len(listaPos))
print(listaNum)

#Suma Total
listaNum = [1,3,5,6,7,9,2,1,4]
suma = 0
for num in listaNum:
    suma += num
print(suma)
print(sum(listaNum))

#promedio
listaNum = [1,3,5,6,7,9,2,1,4]
suma = 0
for num in listaNum:
    suma += num
print(sum(listaNum)/ len(listaNum))

#Longitud
listaNum = [1,3,5,6,7,9,2,1,4]
print(len(listaNum))

#Minimo y Maximo
listaNum = [1,3,5,6,7,9,2,1,4]

def minimoYmaximo (listaNum):
    print (min(listaNum))
    print (max(listaNum))

minimoYmaximo (listaNum)

#Análisis final
listaNum = [1,3,5,6,7,9,2,1,0,4,10,11,34,56,43,21,18]
analisisFinal={"suma":0 , "Promedio":0 , "Maximo":0 , "Minimo":0 }
for num in listaNum:
    analisisFinal ["suma"] = sum(listaNum)
    analisisFinal ["Promedio"]= promedio=((sum(listaNum)/ len(listaNum)))
    analisisFinal ["Minimo"]=minimo=(min(listaNum))
    analisisFinal ["Maximo"]=maximo=(max(listaNum))

print(analisisFinal)

#Lista inversa
listaNum = [1,3,5,6,7,9,2,1,0,4,10,11,34,56,43,21,18]
ListaNum=list(reversed(listaNum))

print(ListaNum)