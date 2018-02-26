import os
def imp_version():
	return 1.0

def crea_dir(dir):
	if os.access("/tmp/"+dir,1):
		return "La carpeta YA existe"
	os.mkdir("/tmp/"+dir)
	return "La carpeta ha sido creada"

def entorno():
	diccionario_retorno = {}
	for clave,valor in os.environ.iteritems():
		if clave == "USER":
			diccionario_retorno['USUARIO'] = valor
		if clave == "SHELL":
			diccionario_retorno['SHELL'] = valor
		if clave == "PATH":
			diccionario_retorno['PATH'] = valor
	return diccionario_retorno

def gordos(directorio,size):
	limpiar()
	for elemento in os.listdir(directorio):
		medida = size[-1:]
		ruta = directorio+"/"+elemento
		if os.path.isfile(ruta):
			if os.path.getsize(ruta) > int(size[:-1]):
				if medida == "K":
					pesofinal = float(os.path.getsize(ruta))/1024
					print elemento+" "+str(pesofinal)+medida

def limpiar():
	os.system("clear")

def visualizar(fichero):
	archivo = open(fichero,"r")
	contenido = archivo.read()
	archivo.close()
	return contenido

def cp(fichero1,fichero2):
	if os.access(fichero1,0):
		archivo1 = open(fichero1,"r")
		archivo2 = open(fichero2,"a")
		while True:
			linea = archivo1.readline()
			if not linea:break
			archivo2.write(linea)
		archivo1.close()
		archivo2.close()
