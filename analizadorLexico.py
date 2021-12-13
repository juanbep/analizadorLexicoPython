# 'w' ----> la 'w' crea o sobrescribe el archivo con la actulizacion que le hayamos hecho  
# 'a' ----> la 'a' agrega una nueva linea
# 'x' ----> la 'x' crea un archivo desde cero
# 'r' ----> la 'r' para abrir un archivo en modo lectura


#funcion para eliminar las lineas vacias del pseudocodigo, esto por temas de practicidad...
def clearBlankline(infile,outfile):
	infopen=open(infile,'r',encoding='utf-8')
	outopen=open(outfile,'w',encoding='utf-8')
	lines=infopen.readlines()
	for line in lines:
		if line.split():
			outopen.writelines(line)
		else:
			outopen.writelines("")
	infopen.close()
	outopen.close()

tablaLexica = 'tablaLexica.txt' # archivo txt de la tabla lexica 
pseudocodigo = 'pseudocodigo.txt' #archvio txt del pseucodigo 
psAuxiliar = 'psAuxiliar.txt' #archivo auxiliar txt donde vamos a guardar el pseudocodigo pero sin espacios, y el que vamos a usar para trabajar a lo largo de nuestro programa 
codigoPython = 'codigoPython.py' #archivo .py en donde vamos a guardar el pseudocodigo ya traducido a python
f = open(tablaLexica, 'r') #abrimos la tabla lexica en modo lectura 
h = open(codigoPython, 'r') #abrimos el archivo "codigoPython" en modo lectura 
clearBlankline(pseudocodigo, psAuxiliar) #invocamos la funcion para borrar las linas en blanco del pseudocodigo y guardamos el pseudocodigo sin lineas en blanco en "psAuxiliar"
g = open(psAuxiliar, 'r') #abrimos el archivo "psAuxiliar en modo lectura"
lpsAuxiliar = g.readlines()
lTablaLexica = f.readlines()
lcodigoPython = h.readlines()
iniLineaUno = True
comentario = False
palabras = []
encontrada = False


	
#este primer ciclo for se encarga de importar las librerias necesarias en python 
#para las palabras que así lo requieran 			
for k in range(len(lpsAuxiliar)):
	if "azar" in lpsAuxiliar[k]:
		h = open(codigoPython, 'w')
		h.write("import random\n")
		iniLineaUno = False

for i in range(8):
	cadenaLps = lpsAuxiliar[i] #contiene una linea del pseudocodigo en la posicion i 
	cadenaTlexica = lTablaLexica[0] #contienen una linea de la tabla lexica en la posicion i 
	esComentario = cadenaLps[0:2]
	comentario = False
	if esComentario == cadenaTlexica[0:2]:
		if iniLineaUno == True:
			h = open(codigoPython, 'w')
			h.write(cadenaTlexica[3]+str(cadenaLps[2:]))
			iniLineaUno = False
		else:
			h = open(codigoPython, 'a')
			h.write(cadenaTlexica[3]+str(cadenaLps[2:]))
		comentario = True
	palabras = cadenaLps.split()
	if comentario == False:		
		for j in range(len(palabras)):
			encontrada = False
			for k in range(len(lTablaLexica)):
				claveLexica = lTablaLexica[k]
				claveLexica = claveLexica.split()
				if palabras[j].upper() == claveLexica[0].upper():
					if palabras[j].upper() == "AZAR":
						h = open(codigoPython, 'a')
						h.write(claveLexica[1])
						encontrada = True
					elif palabras[j].upper() == "LEER":
						h = open(codigoPython, 'a')
						h.write(palabras[j+1]+" = "+claveLexica[1]+"()")
						encontrada = True	
					else:	
						h = open(codigoPython, 'a')
						h.write(claveLexica[1]+" ")
						encontrada = True
			if encontrada == False:
				if palabras[j-1].upper() == "PROCESO":
					h = open(codigoPython, 'a')
					h.write(palabras[j]+"():")
				elif palabras[j-1].upper() == "ESCRIBIR":
					indice = j
					cadena = palabras[indice:]
					strC = " ".join(cadena)
					h = open(codigoPython, 'a')
					h.write("("+strC+")")
					break
				elif palabras[j-1].upper() == "LEER":
					break
				else:		
					h = open(codigoPython, 'a')
					h.write(palabras[j]+" ")
		h = open(codigoPython, 'a')
		h.write("\n")			


	









