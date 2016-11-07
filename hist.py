#!/bin/usr/python
#-*- coding: utf-8 -*-
#Jan Horbowicz
plik=open('cwiczenie1.txt','r') 
tekst=plik.read()
plik.close()
tekst=tekst.translate(None, ",!.;-\\—\"") #translate zmienia wszystkie znaki ze stringa po prawej na None
words = tekst.split()
bezpowtorki = list(set(words))
slow1={}
for i in range(0,len(bezpowtorki)):
	slow1[bezpowtorki[i]]=0
for i in range(0, len(words)):
	slow1[words[i]]+=1
lista = slow1.keys()
for i in range(0,len(bezpowtorki)):
	print lista[i], slow1[lista[i]]
