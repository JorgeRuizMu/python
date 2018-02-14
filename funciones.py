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