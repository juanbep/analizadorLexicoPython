import random
#AdivinaNumero Pseudocodigo
#Juego simple que pide al usuario que adivine un numero en 10 intentos
def Adivina_Numero():
intentos = 10 
num_secreto = random.randint(1,100) 
print ("Adivine el numero(de 1 a 100):")
num_ingresado = imput()
while num_secreto<>num_ingresado and intentos>1 : 
