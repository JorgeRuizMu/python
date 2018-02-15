import os
def imp_version():
	return 1.0

def crea_dir(dir):
	if os.access("/tmp/"+dir,1):
		return "La carpeta YA existe"
	os.mkdir("/tmp/"+dir)
	return "La carpeta ha sido creada"

