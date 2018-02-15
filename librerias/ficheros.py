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
		ruta = directorio+"/"+elemento
		if os.path.isfile(ruta):
			if os.path.getsize(ruta) > int(size):
				print elemento+" "+str(os.path.getsize(ruta))

def limpiar():
	os.system("clear")
