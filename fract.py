#!/usr/bin/python
#Jan Horbowicz
i,lista=1,[]
while (1):	
	if 123456%i==0:
		lista.append(i)
	if len(lista)==28:
		break
	i+=1	
print lista
