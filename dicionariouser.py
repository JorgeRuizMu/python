import librerias.ficheros
import os

os.system("clear")
for clave, valor in librerias.ficheros.entorno().iteritems():
	print clave+" "+valor

