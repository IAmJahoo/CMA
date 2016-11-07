#!/bin/usr/python
#Jan Horbowicz
n = int(raw_input("podaj liczbe, ktorej chcesz obliczyc silnie \n"))
buff = 1
for i in range (1,n+1):
	buff*=i
print '\n',buff

