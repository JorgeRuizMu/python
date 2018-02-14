def imprimir():
	print "hola"
	
def funcion():
	return "Hola mundo"
	
def parimpar(num):
	if num%2 == 0:
		resultado = "par"
	else:
		resultado = "impar"
	return resultado

def par_impar(num):
	resultado = "par" if(num%2==0) else "impar"
	return resultado

def alta_cliente(dni,nombre,*apellidos):
	print dni
	print nombre
	for parametro in apellidos:
		print parametro
		
def iniciales(nombre,*apellidos):
	iniciales =  nombre[:1]
	for apellido in apellidos:
		iniciales = iniciales+"."+apellido[:1]
	return iniciales.upper()