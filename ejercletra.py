import os
letra = raw_input("Dime una letra: ")
dir_list = os.listdir("c:\windows\system32")
num = 0
for e in dir_list:
	if e.count(letra) > 0:
		num +=1
		print e
print "La letra '"+letra+"' aparece en "+str(num)+" archivos"