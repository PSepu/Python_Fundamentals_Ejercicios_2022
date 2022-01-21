
import random
def randInt(min= 0, max=100):
    num = random.random()* (max-min) + min
    if min > max:
        print("Error el minimo no puede ser mayor al maximo")
    if max<0:
        print("Error el maximo no puede ser igual a 0")
    return num
    
#print(randInt()) 		# debería imprimir un número aleatorio entre 0 a 100
#print(randInt(max=50)) 	# debería imprimir un número aleatorio entre 0 a 50
#print(randInt(min=50)) 	# debería imprimir un número aleatorio entre 50 a 100
#print(randInt(min=50, max=500))    # debería imprimir un número aleatorio entre 50 y 500
print(randInt(min=200))    # caso extremo min>max
#print(randInt(max=-50))  # caso extremo max<0

