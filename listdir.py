import os
ext = ("exe","dll","msi")
for ex in ext:
	for e in os.listdir("c:\windows\system32"):
		if e[-3:] == ex:
			print e