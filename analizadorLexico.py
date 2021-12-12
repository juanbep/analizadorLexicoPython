# 'w' ----> la 'w' crea o sobrescribe el archivo con la actulizacion que le hayamos hecho  
# 'a' ----> la 'a' agrega una nueva linea
# 'x' ----> la 'x' crea un archivo desde cero
# 'r' ----> la 'r' para abrir un archivo en modo lectura


#funcion para eliminar las lineas vacias 
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


tablaLexica = 'tablaLexica.txt'
pseudocodigo = 'pseudocodigo.txt'
psAuxiliar = 'psAuxiliar.txt'
codigoPython = 'codigoPython.py'
f = open(tablaLexica, 'r')
h = open(codigoPython, 'r')
clearBlankline(pseudocodigo, psAuxiliar)
g = open(psAuxiliar, 'r')
lpsAuxiliar = g.readlines()
lTablaLexica = f.readlines()
lcodigoPython = h.readlines()
iniLineaUno = True
comentario = False
palabras = []


for i in range(3):
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
			for k in range(len(lTablaLexica)):
				claveLexica = lTablaLexica[k]
				claveLexica = claveLexica.split()
				if palabras[j].upper() == claveLexica[0].upper():
					print("si es")



#len(lpsAuxiliar)
	









