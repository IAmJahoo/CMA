#!/usr/bin/python
#Jan Horbowicz
def fibb(n):    
    a,b=0,1
    print 1,a,"\n",2,b
    for i in range(2,n):
        c=a+b
        print i+1, c
        a=b
        b=c         
x = int(raw_input("Podaj zakres ciagu \n"))
fibb(x)
