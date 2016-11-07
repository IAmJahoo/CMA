#!/usr/bin/python
#Jan Horbowicz
lista, a= [2], 3
while len(lista)<6000:
	for i in range(2,a):
		if a%i==0:
			break
		elif i==a-1:
			lista.append(a)
	a+=1
print lista, len(lista)
				
		
