import sys
import librerias.ficheros
if len(sys.argv) == 2:
	print librerias.ficheros.crea_dir(sys.argv[1])
else:
	print "Necesito un directorio"
