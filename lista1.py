#Los datos en las listas si se pueden variar una vez definidos, se ponen entre corchetes
mi_lista = ["jorge","ruiz","munyoz"]
print mi_lista[2]
for datos in mi_lista:
	print datos
mi_lista[1] = "cambiado"
print mi_lista[1]
for datos in mi_lista:
	print datos