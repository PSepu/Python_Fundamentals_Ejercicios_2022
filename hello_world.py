# 1. TAREA: imprimir "Hola mundo"
print( "Hola Mundo" )
# 2. imprimir "Hola Noelle!" con el nombre en una variable
nombre= "Pablo"
print( "hola", nombre)	# con una coma
print( "hola" +" "+ nombre)	# con un +
# 3. imprimir "Hola 42!" con un numero en una variable
num = 26
print( "hola", num )	# con una coma
print(f"hola {num}")	# con un + - !Este debería darnos un error!
# 4. imprimir "Me encanta comer sushi and pizza." con los alimentos en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print( "Me encanta comer", fave_food1, "y", fave_food2 ) # con .format()
print( f"Me encanta comer {fave_food1} y {fave_food2}" ) # con una cadena f
