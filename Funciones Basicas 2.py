# Cuenta regresiva 
from tkinter import Y
x=10
for x in range(x,0,-1):
    print(x-1)

# Imprimir y volver
def a(b,c):
    print(b)
    return c
print(a(3,5))

#First Plus Length
x = [8, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length = len(x)

print(x[0])
print(length)
print(x[0]+length)

#Valores mayores que el segundo

x= [1,4,3,4,5,4,8,3,2,6,1]
segundoNum=x[1]
y = []
for num in x:
    if (segundoNum < num):
        y.append(num)
print(len(y))
print(y)

# Esta longitud, ese valor

x = []
def longitudyValor(a,b):
    for i in range (a):
        x.append(b)
    print(x)

longitudyValor(5,7)

