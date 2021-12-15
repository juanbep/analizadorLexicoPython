import random
#AdivinaNumero Pseudocodigo
#Juego simple que pide al usuario que adivine un numero en 10 intentos
def Adivina_Numero() :
intentos = 10 
num_secreto = random.randint(1,100) 
print (" Adivine el numero(de 1 a 100): (" 
num_ingresado = input()
while num_secreto != num_ingresado and intentos > str(1) : 
if str(num_secreto) > str(num_ingresado) : 
print (" Muy bajo (" 
else: 
print (" Muy alto (" 
#finsi 
intentos = intentos-1 
print (" Le quedan (" + str(intentos) + (" intentos: (" 
num_ingresado = input()
#finmientras 
if str(num_secreto) == num_ingresado : 
print (" Exacto! Usted adivino en (" + str(11-intentos) + (" intentos. (" 
else: 
print (" El numero era: (" + str(num_secreto) 
#finsi 
